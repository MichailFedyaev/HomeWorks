from src.product import Product


def test_product_initialization(product, product1):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5

    assert product1.name == "Iphone 15"
    assert product1.description == "512GB, Gray space"
    assert product1.price == 210000.0
    assert product1.quantity == 8


def test_product_creation(products):
    assert len(products) == 4  # Проверяем, что всего создано 4 продукта
    assert products[0].name == "Samsung Galaxy C23 Ultra"
    assert products[1].price == 210000.0
    assert products[2].quantity == 14
    assert products[3].description == "Фоновая подсветка"


def test_product_properties(products):
    assert products[0].name == "Samsung Galaxy C23 Ultra"
    assert products[0].description == "256GB, Серый цвет, 200MP камера"
    assert products[0].price == 180000.0
    assert products[0].quantity == 5

    product2 = products[3]
    assert product2.name == "55\" QLED 4K"
    assert product2.quantity == 7


def test_new_product(product_dict):
    product4 = Product.new_product(product_dict)
    assert product4.name == "Xiaomi Redmi Note 11"
    assert product4.description == "1024GB, Синий"
    assert product4.price == 31000.0
    assert product4.quantity == 14


def test_prod_price_property(capsys, product):
    product.price = -756.57
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    product.price = 756.57
    assert product.price == 756.57


def test_product_price_setter(product):
    assert product.price == 180000.0
    product.price = -50
    assert product.price == 180000.0
    product.price = 0
    assert product.price == 180000.0
    product.price = 150
    assert product.price == 150.0


def test_product_str(first_product):
    assert str(first_product) == "Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт."


def test_product_add(first_product, second_product):
    assert first_product + second_product == 1334000
