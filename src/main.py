from scraper import Scraper
from csv_writer import save_products_to_csv

URL = "https://www.euro.com.pl/laptopy-i-netbooki.bhtml"


def main():
    scraper = Scraper(URL)

    try:
        products = scraper.scrape_page()

        print(f"Found {len(products)} products")

        save_products_to_csv(products, "data/laptops.csv")

    finally:
        scraper.close()


if __name__ == "__main__":
    main()
