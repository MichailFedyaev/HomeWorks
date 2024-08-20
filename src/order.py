from src.order_category_property import OrderCategoryProperties
from src.product import Product


class Order(OrderCategoryProperties):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int):
        if quantity > product.quantity:
            raise ValueError(
                f"Товар {product.name} на данный момент доступен только в количестве " f"{product.quantity} штук."
            )

        product.quantity -= quantity

        self.product = product
        super().__init__(product.name, product.description)
        self.quantity = quantity
        self.total_price = self.product.price * self.quantity

    def __str__(self) -> str:
        return (
            f"Куплено: {self.name}, {self.quantity} шт.\n"
            f"Описание товара: {self.description}\n"
            f"Сумма покупки: {round(self.total_price)} руб"
        )
