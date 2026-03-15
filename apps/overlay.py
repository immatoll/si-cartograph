import webview

def main():
    webview.create_window(
        "SILVER.INTEL.CARTOGRAPH",
        "https://www.silver-tribe.com/cartograph",
        width=480,
        height=710,
        frameless=False,
        on_top=True,
    )
    webview.start()


if __name__ == "__main__":
    main()