from src.base_order import Abstract
from src.product import Product


class Order(Abstract):
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = self.quantity * product.price

    def __str__(self):
        return f"{self.product.name}, куплено - {self.quantity} штук, итоговая стоимость - {self.total_price} рублей"
