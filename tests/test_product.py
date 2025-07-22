import pytest
from unittest.mock import patch
from src.product import Product


def test_product_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_new_product_1(product_dict_1):
    existing_products = [
        Product(name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=170000.0,
                quantity=2)
    ]
    product = Product.new_product(product_dict_1, existing_products)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 7


def test_product_str(product_1):
    assert str(product_1) == 'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.'


def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 1260000.0


def test_product_smartphone_add(product_smartphone_1, product_smartphone_2):
    assert product_smartphone_1 + product_smartphone_2 == 2580000.0


def test_product_lawn_grass_add(product_lawn_grass_1, product_lawn_grass_2):
    assert product_lawn_grass_1 + product_lawn_grass_2 == 16750.0


def test_product_smartphone_add_error(product_smartphone_1):
    with pytest.raises(TypeError):
        result = product_smartphone_1 + 4


def test_new_product_2(product_dict_2):
    existing_products = [
        Product(name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=170000.0,
                quantity=2)
    ]
    product = Product.new_product(product_dict_2, existing_products)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 180000.0
    assert product.quantity == 2


def test_new_product_none(product_dict_1):
    existing_products = None
    product = Product.new_product(product_dict_1, existing_products)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def assert_print_called_with(mock_print, expected_calls):
    for expected_call in expected_calls:
        mock_print.assert_any_call(expected_call)


@pytest.mark.parametrize("price, expected_messages", [
    (0, ["Цена не должна быть нулевая или отрицательная"]),
    (-180000.0, ["Цена не должна быть нулевая или отрицательная"]),
])
def test_price_change_to_zero_or_negative(price, expected_messages, product_1):
    product = Product("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5)

    with patch('builtins.print') as mock_print:
        product.price = price
        assert_print_called_with(mock_print, expected_messages)


@pytest.mark.parametrize("new_price, user_response, expected_final_price, expected_message", [
    (170000.0, 'y', 170000.0, "Цена успешно изменена на 170000.0"),
    (160000.0, 'n', 180000.0, "Цена не была изменена."),
])
def test_price_decrease_with_confirmation(new_price, user_response, expected_final_price, expected_message):
    product = Product("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5)

    with patch('builtins.input', return_value=user_response), patch('builtins.print') as mock_print:
        product.price = new_price
        assert product.price == expected_final_price
        mock_print.assert_called_with(expected_message)
