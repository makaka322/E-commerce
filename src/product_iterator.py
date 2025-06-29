from src.product import Product
from src.category import Category


class ProductIterator:
    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.category.products_list):
            products = self.category.products_list[self.index]
            self.index += 1
            return products
        else:
            raise StopIteration
