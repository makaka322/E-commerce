import pytest
from src.product import Product
from src.category import Category
from src.product_iterator import ProductIterator
from src.new_product import Smartphone, LawnGrass


@pytest.fixture
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=180000.0, quantity=2)


@pytest.fixture
def product_dict_1():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def product_dict_2():
    return {"name": "Iphone 15", "description": "512GB, Gray space", "price": 180000.0, "quantity": 2}


@pytest.fixture
def category_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения доп. функций",
        products=[
            Product(
                name="Samsung Galaxy S23 Ultra",
                description="256GB, Серый цвет, 200MP камера",
                price=180000.0,
                quantity=5,
            ),
            Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8),
        ],
    )


@pytest.fixture
def product_iterator(category_1):
    return ProductIterator(category_1)

@pytest.fixture
def all_products():
    Category.product_count = 0
    product1 = Product("Samsung", "Серый цвет", 18, 5)

    category1 = Category("Смартфоны", "Смартфоны, как средство", [product1])
    return category1

@pytest.fixture
def product_smartphone_1():
    return Smartphone(name="Samsung Galaxy S23 Ultra",
                      description="256GB, Серый цвет, 200MP камера",
                      price=180000.0,
                      quantity=5,
                      efficiency=95.5,
                      model="S23 Ultra",
                      memory=256,
                      color="Серый")


@pytest.fixture
def product_smartphone_2():
    return Smartphone(name="Iphone 15",
                      description="512GB, Gray space",
                      price=210000.0,
                      quantity=8,
                      efficiency=98.2,
                      model="15",
                      memory=512,
                      color="Gray space")


@pytest.fixture
def product_lawn_grass_1():
    return LawnGrass(name="Газонная трава",
                     description="Элитная трава для газона",
                     price=500.0,
                     quantity=20,
                     country="Россия",
                     germination_period="7 дней",
                     color="Зеленый")


@pytest.fixture
def product_lawn_grass_2():
    return LawnGrass(name="Газонная трава 2",
                     description="Выносливая трава",
                     price=450.0,
                     quantity=15,
                     country="США",
                     germination_period="5 дней",
                     color="Темно-зеленый")

