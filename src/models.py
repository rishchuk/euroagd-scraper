from dataclasses import dataclass


@dataclass
class Product:
    title: str
    price: str
    image_url: str
    specifications: dict[str, str]
