from bs4 import BeautifulSoup, Tag


def get_products(html: str) -> list[Tag]:
    """
    Return all products from the page
    """
    soup = BeautifulSoup(html, "html.parser")
    products = soup.find_all("div", class_="product-medium-box")
    return products


def parse_title(product: Tag) -> str:
    """
    Extract product title
    """
    title = product.find("a", class_="product-medium-box-intro__link")
    if title is None:
        return ""

    return title.get_text(strip=True)
