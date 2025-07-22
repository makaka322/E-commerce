from src.order import Order


def test_order(product_1):
    quantity = 5
    order = Order(product_1, quantity)
    assert str(order) == "Samsung Galaxy S23 Ultra, куплено - 5 штук, итоговая стоимость - 900000.0 рублей"
