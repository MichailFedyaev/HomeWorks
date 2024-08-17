class Product:
    """Категория продуктов."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name}, {round(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> int:
        if isinstance(other, Product):
            return round(self.price * self.quantity + other.price * other.quantity)
        raise TypeError()

    @classmethod
    def new_product(cls, new_product: dict):
        """Возвращает созданный объект класса Product из параметров товара в словаре."""
        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value
