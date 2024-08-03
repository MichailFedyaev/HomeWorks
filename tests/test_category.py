
def test_category_initialization(category_data):
    """Тест для проверки инициализации категории."""
    assert len(category_data) == 2
    assert category_data[0].name == "Смартфоны"
    assert category_data[1].description == ("Современный телевизор, который позволяет наслаждаться просмотром, станет"
                                            " вашим другом и помощником")


def test_category(first_category, second_category):
    assert first_category.name == "Category"
    assert first_category.description == "Description of the category"
    assert len(first_category.products) == 2

    assert first_category.category_count == 4
    assert second_category.category_count == 4

    assert first_category.product_count == 9
    assert second_category.product_count == 9


def test_category_products(category_data):
    """Тест для проверки продуктов в категориях."""
    assert len(category_data[0].products) == 3
    assert category_data[0].products[0]['name'] == "Samsung Galaxy C23 Ultra"

    assert len(category_data[1].products) == 1
    assert category_data[1].products[0]['name'] == "55\" QLED 4K"
