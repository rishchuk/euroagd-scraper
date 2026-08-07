from browser import create_driver, get_page_html
from parser import get_products


URL = "https://www.euro.com.pl/laptopy-i-netbooki.bhtml"


def main():
    driver = create_driver()
    html = get_page_html(driver, URL)

    products = get_products(html)
    print(f"Found {len(products)} products")

    driver.quit()


if __name__ == "__main__":
    main()
