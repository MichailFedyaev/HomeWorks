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
    assert len(first_category.add_product_list) == 2

    assert first_category.category_count == 4
    assert second_category.category_count == 4

    assert first_category.product_count == 9
    assert second_category.product_count == 9


def test_cat_get_product_list_property(first_category, second_category):
    with pytest.raises(AttributeError):
        print(first_category.__products)

    assert (
            first_category.add_product_str
            == "Product, Description of the product руб. Остаток: 10 шт.\n"
               "Product number two, Description of the product number two руб. Остаток: 34 шт.\n"
    )

    assert (
            second_category.add_product_str
            == "Product, Description of the product руб. Остаток: 10 шт.\n"
               "Product number two, Description of the product number two руб. Остаток: 34 шт.\n"
               "Product three, Description of the product three руб. Остаток: 32 шт.\n"
    )
