# Frontier Chat Location WebSocket Tool

A Python tool that watches your **Frontier chat logs** for system location changes and broadcasts the current location over a WebSocket server in real time.

---

## Features

- Monitors the latest `Local_*.txt` chat log file (Windows: "%USERPROFILE%\Documents\Frontier\logs\Chatlogs")
- Detects when the player changes local system channels.
- Broadcasts the current system name and system ID to connected WebSocket clients (e.g. www.silver-tribe.com/scout)
- Automatically detects log file encoding (`UTF-8`, `UTF-16`, `UTF-16-BE`, `UTF-8-SIG`).

Privacy Note: Websocket Server (Python) <> Client (e.g. JavaScript) communication works 

---

## Requirements

- Python 3.10+
- Windows (or modify the chatlog path manually)
- [websockets](https://pypi.org/project/websockets/)
- Optional: [pywebview](https://pypi.org/project/pywebview/) if you want to display the data in a simple GUI overlay.

## Install dependencies:

```bash
pip install websockets pywebview

```bash
pip install -r requirements.txt

---

## Requirements

```bash
python launcher.py (for Websocket + Webviewer)

```bash
python apps/locator.py (for Websocket only)

```bash
python apps/overlay.py (for Overlay only)