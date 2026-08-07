import csv
from models import Product


def save_products_to_csv(products: list[Product], path: str) -> None:
    """
    Save products into CSV file.
    """
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Title",
                "Price",
                "Image URL",
                "Specifications"
            ]
        )

        for product in products:
            writer.writerow(
                [
                    product.title,
                    product.price,
                    product.image_url,
                    product.specifications
                ]
            )
