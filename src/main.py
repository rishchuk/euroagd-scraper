from browser import create_driver, get_page_html


URL = "https://www.euro.com.pl/laptopy-i-netbooki.bhtml"


def main():
    driver = create_driver()
    html = get_page_html(driver, URL)

    print(html)
    driver.quit()


if __name__ == "__main__":
    main()
