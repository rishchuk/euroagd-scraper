from bs4 import BeautifulSoup, Tag
from models import Product


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
    if not title:
        return ""

    return title.get_text(strip=True)


def parse_price(product: Tag) -> str:
    """
    Extract product price
    """
    price_whole = product.find("span", class_="parted-price-total")

    price_decimal = product.find("span", class_="parted-price-decimal")

    currency = product.find("span", class_="parted-price-currency")

    if not price_whole:
        return ""

    whole = price_whole.get_text(strip=True)
    decimal = price_decimal.get_text(strip=True)
    currency_text = currency.get_text(strip=True)

    return f"{whole}.{decimal} {currency_text}"


def parse_img_url(product: Tag) -> str:
    """
    Extract product image URL
    """
    image = product.find("div", class_="product-medium-box-content__photo-wrapper")
    if not image:
        return ""

    img = image.find("img")
    if not image:
        return ""

    return img.get("src")


def parse_specifications(product: Tag) -> dict[str, str]:
    """
    Extract product specifications
    """
    specefications = {}
    items = product.find_all("div", "technical-attributes-list__item")

    for item in items:
        label = item.find("dt", "technical-attributes-list__label")

        value = item.find("dd", "technical-attributes-list__value")

        if not label or not value:
            continue

        specefications[label.get_text(strip=True)] = value.get_text(strip=True)

    return specefications


def parse_product(product: Tag) -> Product:
    """
    Convert HTML product into Product object
    """
    return Product(
        title=parse_title(product),
        price=parse_price(product),
        image_url=parse_img_url(product),
        specifications=parse_specifications(product)
    )
