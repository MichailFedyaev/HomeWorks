import pytest


def test_category_initialization(category_data):
    """Тест для проверки инициализации категории."""
    assert len(category_data) == 2
    assert category_data[0].name == "Смартфоны"
    assert category_data[1].description == ("Современный телевизор, который позволяет наслаждаться просмотром, станет"
                                            " вашим другом и помощником")


def test_category(first_category, second_category):
    assert first_category.name == "Category"
    assert first_category.description == "Description of the category"
    assert len(first_category.product_list) == 2

    assert first_category.category_count == 6
    assert second_category.category_count == 6

    assert first_category.product_count == 12
    assert second_category.product_count == 12


def test_cat_get_product_list_property(first_category, second_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)
    assert (
        first_category.product_str
        == "Product, 84 руб. Остаток: 10 шт.\nProduct number two, 156 руб. Остаток: 34 шт.\n"
    )
    assert (
        second_category.product_str
        == "Product, 84 руб. Остаток: 10 шт.\nProduct number two, 156 руб. Остаток: 34 шт."
        "\nProduct three, 8468 руб. Остаток: 32 шт.\n"
    )


def test_category_str(first_category, second_category):
    assert str(first_category) == "Category, количество продуктов: 44 шт."
    assert str(second_category) == "Category number two, количество продуктов: 76 шт."
