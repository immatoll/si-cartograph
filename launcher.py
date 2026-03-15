import threading
import sys

from apps.locator import main as locator_main
from apps.overlay import main as overlay_main


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
    print("Starting overlay...")
    print(f"Frameless mode: {frameless}")

    try:
        overlay_main(frameless=frameless)
    except KeyboardInterrupt:
        print("\nStopping application...")


if __name__ == "__main__":
    main()