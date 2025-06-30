import pytest

from src.category import Category
from src.product import Product
from src.product_iterator import ProductIterator


def test_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации, но и получения доп. функций"
    assert len(category_1.product) == 95
    assert category_1.category_count == 1
    assert category_1.product_count == 2


def test_category_str(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 13 шт"


@pytest.fixture
def all_products():
    product1 = Product("Samsung", "Серый цвет", 18, 5)

    category1 = Category("Смартфоны", "Смартфоны, как средство", [product1])
    return category1


def test_add_product(all_products):
    product4 = Product("QLED", "Фоновая подсветка", 12, 7)
    all_products.add_product(product4)
    assert Category.product_count == 2


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(product_iterator)
