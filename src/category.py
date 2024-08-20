from src.product import Product
from typing import List
from src.order_category_property import OrderCategoryProperties


class Category(OrderCategoryProperties):
    """Категория товара"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        total = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в экземпляр класса Category."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError()

    @property
    def product_str(self) -> str:
        """Геттер для получения списка продуктов в виде строк."""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def product_list(self) -> List[Product]:
        """Геттер для получения списка продуктов."""
        return self.__products
