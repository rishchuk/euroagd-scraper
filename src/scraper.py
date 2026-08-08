from browser import create_driver, get_page_html
from parser import get_products, parse_product
from models import Product
from logger import logger


class Scraper:
    """
    Main scraper class
    Responsible for collecting products
    """
    def __init__(self, url: str):
        self.url = url
        self.driver = create_driver()

    def scrape_page(self) -> list[Product]:
        """
        Scrape one page
        """
        html = get_page_html(self.driver, self.url)

        product_cards = get_products(html)

        products = []
        for card in product_cards:
            product = parse_product(card)
            products.append(product)

        return products

    def build_page_url(self, page: int) -> str:
        """
        Build URL for pagination
        """
        if page == 1:
            return self.url

        return self.url.replace(".bhtml", f",strona-{page}.bhtml")

    def scrape_all_pages(self, start_page: int = 1) -> list[Product]:
        """
        Scrape all pages until no products found
        """
        all_products = []
        page = start_page

        while True:
            url = self.build_page_url(page)

            logger.info(f"Scraping page {page}")

            try:
                html = get_page_html(self.driver, url)
            except Exception as error:
                print(error)
                break

            product_cards = get_products(html)

            if not product_cards:
                print("No products found. Finished.")
                break

            for card in product_cards:
                product = parse_product(card)
                all_products.append(product)

            print(f"Total products: {len(all_products)}")

            page += 1

        return all_products

    def close(self):
        self.driver.quit()
