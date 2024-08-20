class PrintMixin:
    """Класс-миксин, который печатает в консоль информацию о инициализации экземпляров класса"""

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"