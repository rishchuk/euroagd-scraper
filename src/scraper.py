from browser import create_driver, get_page_html
from parser import get_products, parse_product
from models import Product


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

    def close(self):
        self.driver.quit()
