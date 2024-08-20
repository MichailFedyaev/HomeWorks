import pytest

from src.order import Order
from src.smartphone import Smartphone


def test_order_init(smartphone1: Smartphone) -> None:

    quantity = smartphone1.quantity
    order1 = Order(smartphone1, 3)

    assert quantity - 3 == smartphone1.quantity

    assert order1.product.price == smartphone1.price
    assert order1.name == smartphone1.name
    assert order1.description == smartphone1.description
    assert order1.quantity == 3
    assert order1.total_price == 150_000


def test_order_init_error(smartphone1: Smartphone) -> None:
    with pytest.raises(ValueError):
        Order(smartphone1, 6)


def test_order_str(smartphone1: Smartphone) -> None:

    order1 = Order(smartphone1, 2)

    info_string = str(order1)
    expected = "Куплено: Smartphone1, 2 шт.\n" "Описание товара: Description1\n" "Сумма покупки: 100000 руб"

    assert info_string == expected
