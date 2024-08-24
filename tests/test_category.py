import pytest
from src.category import Category
from src.product import Product


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


def test_category_add_product_zero_error(capsys, categories):
    product = Product("Тест","Количество: 0", 10, 1)
    product.quantity = 0
    categories[0].add_product(product)

    message = capsys.readouterr()
    failed, completed = message.out.strip().split("\n")[1:]

    assert Category.product_count == 3

    assert failed == "Невозможно добавить товар с нулевым количеством"

    assert completed == "Обработка добавления товара завершена."


def test_category_add_produuct(capsys, categories: tuple, products: tuple) -> None:
    categories[0].add_product(products[2])

    message = capsys.readouterr()
    messages = message.out.strip().split("\n")

    successfully = messages[0] if len(messages) > 0 else ""
    completed = messages[1] if len(messages) > 1 else ""

    assert Category.product_count == 4
    assert successfully == "Товар 'Xiaomi Redmi Note 11' успешно добавлен."
    assert completed == "Обработка добавления товара завершена."


def test_middle_price_empy():
    category = Category("Category", "Description", [])
    assert category.middle_price() == 0


def test_middle_price(categories):
    assert categories[0].middle_price() == 171_000.0

