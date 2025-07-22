def test_product_smartphone_init(product_smartphone_1):
    assert product_smartphone_1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone_1.price == 180000.0
    assert product_smartphone_1.quantity == 5
    assert product_smartphone_1.efficiency == 95.5
    assert product_smartphone_1.model == "S23 Ultra"
    assert product_smartphone_1.memory == 256
    assert product_smartphone_1.color == "Серый"


def test_product_lawn_grass_init(product_lawn_grass_1):
    assert product_lawn_grass_1.name == "Газонная трава"
    assert product_lawn_grass_1.description == "Элитная трава для газона"
    assert product_lawn_grass_1.price == 500.0
    assert product_lawn_grass_1.quantity == 20
    assert product_lawn_grass_1.country == "Россия"
    assert product_lawn_grass_1.germination_period == "7 дней"
    assert product_lawn_grass_1.color == "Зеленый"
