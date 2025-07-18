from src.base_product import BaseProduct
from src.product import Product
from typing import List

class Category(BaseProduct):
    name: str
    description: str
    products: List[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_products} шт"

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Ожидается объект типа Product")

    @property
    def product(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        return self.__products

