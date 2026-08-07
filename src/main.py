from scraper import Scraper

URL = "https://www.euro.com.pl/laptopy-i-netbooki.bhtml"


def main():
    scraper = Scraper(URL)

    try:
        products = scraper.scrape_page()

        print(f"Found {len(products)} products")

        for product in products:
            print(product)

    finally:
        scraper.close()


if __name__ == "__main__":
    main()
