import asyncio
import json
from pathlib import Path
import re
import os
import websockets

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
SYSTEM_LABELS_FILE = BASE_DIR / "systems.json"

LOG_FOLDER = Path(os.path.expandvars(r"%USERPROFILE%\Documents\Frontier\logs\Chatlogs"))

# -----------------------------
# Globals
# -----------------------------
SYSTEM_IDS = {}
clients = set()
last_location_message = None
latest_file = None
current_system = None

# -----------------------------
# Load system labels
# -----------------------------
with open(SYSTEM_LABELS_FILE, "r", encoding="utf-8") as f:
    SYSTEM_IDS = json.load(f)


# -----------------------------
# Utility: open log with correct encoding
# -----------------------------
def open_log(path):
    with open(path, "rb") as f:
        start = f.read(4)

    if start.startswith(b"\xff\xfe"):
        encoding = "utf-16"
    elif start.startswith(b"\xfe\xff"):
        encoding = "utf-16-be"
    elif start.startswith(b"\xef\xbb\xbf"):
        encoding = "utf-8-sig"
    else:
        encoding = "utf-8"

    return open(path, "r", encoding=encoding, errors="ignore")


# -----------------------------
# Broadcast current system to WebSocket clients
# -----------------------------
async def broadcast_system(system_name):
    global last_location_message

    system_id = None
    for sid, name in SYSTEM_IDS.items():
        if name == system_name:
            system_id = sid
            break

    if not system_id:
        system_id = "unknown"

    message = json.dumps({"system": system_name, "system_id": system_id})
    last_location_message = message

    if clients:
        dead_clients = set()

        for client in clients:
            try:
                await client.send(message)
            except Exception:
                dead_clients.add(client)

        for client in dead_clients:
            clients.discard(client)


# -----------------------------
# Watch chat log for location changes
# -----------------------------
async def watch_file(file_path):
    global current_system

    with open_log(file_path) as f:
        f.seek(0, 2)

        while True:
            line = f.readline()
            if not line:
                await asyncio.sleep(0.5)
                continue

            match = re.search(r"Channel changed to Local : (.+)", line)
            if match:
                location = match.group(1).strip()
                if location != current_system:
                    current_system = location
                    print("Location changed:", location)
                    await broadcast_system(location)


# -----------------------------
# Find latest chat log file
# -----------------------------
def find_latest_file():
    files = list(LOG_FOLDER.glob("Local_*.txt"))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


# -----------------------------
# WebSocket handler
# -----------------------------
async def websocket_handler(websocket):
    global last_location_message

    clients.add(websocket)
    print("Client connected")

    if last_location_message:
        await websocket.send(last_location_message)

    try:
        await websocket.wait_closed()
    finally:
        clients.discard(websocket)
        print("Client disconnected")


# -----------------------------
# Main async logic
# -----------------------------
async def async_main():
    global latest_file, current_system

    latest_file = find_latest_file()
    if not latest_file:
        print("No log files found!")
        return

    print("Watching file:", latest_file)

    with open_log(latest_file) as f:
        lines = f.readlines()
        for line in reversed(lines):
            match = re.search(r"Channel changed to Local : (.+)", line)
            if match:
                current_system = match.group(1).strip()
                print("Initial location:", current_system)
                await broadcast_system(current_system)
                break

    async with websockets.serve(websocket_handler, "localhost", 9001):
        await watch_file(latest_file)


# -----------------------------
# Public main function
# -----------------------------
def main():
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        print("Exiting locator...")


# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    main()