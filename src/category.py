from src.base_order import Abstract
from src.product import Product
from src.exceptions import ZeroProduct

class Category(Abstract):
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f"{self.name}, количество продуктов: {total_products} шт"

    def add_product(self, product: Product):
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProduct("Нельзя добавляеть товар с нулевым количеством")
            except ZeroProduct as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар успешно добавлен")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self):
        return self.__products

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0

