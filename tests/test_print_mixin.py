from src.product import Product
from src.new_product import Smartphone, LawnGrass


def test_print_mixin(capsys):
    Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone(name="Iphone 15",
               description="512GB, Gray space",
               price=210000.0,
               quantity=8,
               efficiency=98.2,
               model="15",
               memory=512,
               color="Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"

    LawnGrass(name="Газонная трава",
              description="Элитная трава для газона",
              price=500.0,
              quantity=20,
              country="Россия",
              germination_period="7 дней",
              color="Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"


