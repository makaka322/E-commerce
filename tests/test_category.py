from src.category import Category
from src.product import Product
import pytest


def test_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации, но и получения доп. функций"
    assert len(category_1.products) == 95
    assert category_1.category_count == 1
    assert category_1.product_count == 2


@pytest.fixture
def all_products():
    product1 = Product("Samsung", "Серый цвет", 18, 5)

    category1 = Category("Смартфоны", "Смартфоны, как средство", [product1])
    return category1


def test_add_product(all_products):
    product4 = Product("QLED", "Фоновая подсветка", 12, 7)
    all_products.add_product(product4)
    assert Category.product_count == 2