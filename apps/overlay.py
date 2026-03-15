import webview


def main(frameless=False):
    webview.create_window(
        "SILVER.INTEL.CARTOGRAPH",
        "https://www.silver-tribe.com/cartograph",
        width=480,
        height=390,
        frameless=frameless,
        on_top=True,
    )
    webview.start()


if __name__ == "__main__":
    main()