# Frontier Chat Location Parser + WebSocket Server

A Python tool that watches your **Frontier chat logs** for system location changes and broadcasts the current location over a WebSocket server in real time.

<p align="center">
  <img src="assets/1.png" alt="Example">
</p>

---

## Features

### Chat log Reader: 
- Monitors the latest `Local_*.txt` chat log file (Windows: "%USERPROFILE%\Documents\Frontier\logs\Chatlogs")
- Detects when the player changes local system channels.
- Automatically detects log file encoding (`UTF-8`, `UTF-16`, `UTF-16-BE`, `UTF-8-SIG`).

### Websocket (Server): 
- Broadcasts the current system name and system ID to connected WebSocket clients (e.g. `https://www.silver-tribe.com/cartograph`)
- Websocket server runs via `ws://localhost:9001`

### Webviewer Overlay: 
- Simple Webviewer Overlay (Mini-Browser)
- Default-URL: `https://www.silver-tribe.com/cartograph`*
- Default-Settings: `width=480, height=710, frameless=False, on_top=True`

*Note: Websocket Server <> Client communication runs locally within the browser (Python <> JavaScript).

---

## Option 1: Run the executable
Download the latest `si-cartograph.exe` from the [Releases page](https://github.com/immatoll/si-cartograph/releases).

## Option 2: Run from source
1. Clone the repository:
```bash
git clone https://github.com/YourUsername/si-cartograph.git
cd si-cartograph
```
2. Create a virtual environment and install dependencies:
```bash
git clone https://github.com/YourUsername/si-cartograph.git
cd si-cartograph
```
3. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
Run the launcher:
```bash
python launcher.py
```

Or run the individual apps:
```bash
python apps/locator.py
```
```bash
python apps/overlay.py
```

## Requirements

- Python 3.10+
- Windows (or modify the chatlog path manually)
- [websockets](https://pypi.org/project/websockets/)
- [pywebview](https://pypi.org/project/pywebview/)