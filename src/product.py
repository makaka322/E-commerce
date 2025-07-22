from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if quantity == 0:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(other) is self.__class__:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, product_info, existing_products=None):
        existing_products = existing_products if existing_products is not None else []

        for existing_product in existing_products:
            if existing_product.name == product_info.get("name"):
                existing_product.quantity += product_info.get("quantity")
                existing_product.price = max(existing_product.price, product_info.get("price"))
                return existing_product

        return cls(
            name=product_info.get("name"),
            description=product_info.get("description"),
            price=product_info.get("price"),
            quantity=product_info.get("quantity")
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input("Вы действительно хотите понизить цену? (y/n): ")
            if confirmation.lower() == 'y':
                self.__price = value
                print(f"Цена успешно изменена на {self.__price}")
            else:
                print("Цена не была изменена.")
        else:
            self.__price = value
            print(f"Цена успешно изменена на {self.__price}")
