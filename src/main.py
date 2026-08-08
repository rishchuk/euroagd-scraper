from scraper import Scraper
from csv_writer import save_products_to_csv

URL = "https://www.euro.com.pl/laptopy-i-netbooki.bhtml"
CSV_PATH = "data/laptops.csv"


def main():
    scraper = Scraper(URL)

    try:
        products = scraper.scrape_all_pages()

        print(f"Found {len(products)} products")

        save_products_to_csv(products, CSV_PATH)

    finally:
        scraper.close()


if __name__ == "__main__":
    main()
