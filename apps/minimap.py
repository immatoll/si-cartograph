import webview


def create_window(frameless=False):
    webview.create_window(
        "SILVER.INTEL.MINIMAP",
        "https://www.silver-tribe.com/map",
        width=400,
        height=400,
        frameless=frameless,
        on_top=True,
    )


def main(frameless=False):
    create_window(frameless=frameless)
    webview.start()


if __name__ == "__main__":
    main()