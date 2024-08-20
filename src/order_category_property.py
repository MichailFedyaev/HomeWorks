from abc import ABC, abstractmethod


class OrderCategoryProperties(ABC):
    """Абстрактный класс для общих свойств классов Заказ и Категория."""

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass
