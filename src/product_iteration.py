from src.category import Category
from src.product import Product


class ProductIterator:
    """Вспомогательный класс для итерации по товарам в категории."""

    def __init__(self, category: Category) -> None:
        """Dunder-метод для инициализации итератора с объектом категории."""
        self.__category = category
        self.__index = 0

    def __iter__(self) -> "ProductIterator":
        """Dunder-метод для возврата итератора."""
        return self

    def __next__(self) -> Product:
        """Dunder-метод для получения следующего товара в категории."""
        if self.__index < len(self.__category.product_list):
            products = self.__category.product_list[self.__index]
            self.__index += 1
            return products
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = ProductIterator(category1)
    for product in iterator:
        print(product)
