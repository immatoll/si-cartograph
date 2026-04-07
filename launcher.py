import threading
import sys
import webview

from apps.locator import main as locator_main
from apps import overlay, minimap


def run_locator():
    try:
        locator_main()
    except Exception as e:
        print(f"Locator crashed: {e}")


def main():
    # Check whether -frameless was passed
    frameless = "-frameless" in sys.argv

    locator_thread = threading.Thread(target=run_locator, daemon=True)
    locator_thread.start()

    print("Locator started.")
    print("Creating overlay and minimap windows...")
    print(f"Frameless mode: {frameless}")

    try:
        overlay.create_window(frameless=frameless)
        # minimap.create_window(frameless=frameless)
        webview.start()
    except KeyboardInterrupt:
        print("\nStopping application...")


if __name__ == "__main__":
    main()