import pytest


def test_smartphone_init(smartphone1):
    assert smartphone1.name == "Smartphone1"
    assert smartphone1.description == "Description1"
    assert smartphone1.price == 50_000
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == "Model X"
    assert smartphone1.memory == 250
    assert smartphone1.color == "Black"


def test_smartphone_add(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 650_000


def test_smartphone_add_lawn_grass(smartphone1, lawn_grass1):
    with pytest.raises(TypeError):
        smartphone1 + lawn_grass1


def test_smartphone_add_price(smartphone1):
    with pytest.raises(TypeError):
        smartphone1 + 90_000
