import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5)


@pytest.fixture
def category_1():
    return Category(name="Смартфоны",
                    description="Смартфоны, как средство не только коммуникации, но и получения доп. функций",
                    products=[
                             Product(
                                    name="Samsung Galaxy S23 Ultra",
                                    description="256GB, Серый цвет, 200MP камера",
                                    price=180000.0,
                                    quantity=5),
                             Product(
                                    name="Iphone 15",
                                    description="512GB, Gray space",
                                    price=210000.0,
                                    quantity=8)
                         ])


@pytest.fixture
def category_2():
    return Category(name="Телевизоры",
                    description="Современный телевизор, позволяющий наслаждаться просмотром",
                    products=[])
