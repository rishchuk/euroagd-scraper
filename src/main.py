import time

from browser import create_driver, get_page_html
from parser import get_products, parse_title, parse_price

URL = "https://www.euro.com.pl/laptopy-i-netbooki.bhtml"


def main():
    driver = create_driver()
    html = get_page_html(driver, URL)

    products = get_products(html)
    print(f"Found {len(products)} products")

    for product in products:
        print(parse_title(product))
        print(parse_price(product))
        print("-" * 40)

    driver.quit()


if __name__ == "__main__":
    main()
