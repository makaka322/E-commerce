def test_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == "Смартфоны, как средство не только коммуникации, но и получения доп. функций"
    assert len(category_1.products) == 2
    assert category_1.category_count == 1
    assert category_1.product_count == 2
