
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
