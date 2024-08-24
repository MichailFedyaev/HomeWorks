from src.product import Product
from typing import List
from src.order_category_property import OrderCategoryProperties
from src.quantity_error import IncorrectProductQuantityError


class Category(OrderCategoryProperties):
    """Категория товара"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list[Product]

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
            try:
                if product.quantity == 0:
                    raise IncorrectProductQuantityError()
            except IncorrectProductQuantityError as e:
                print(e)
            else:
                self.__products.append(product)
                Category.product_count += 1
                print(f"Товар '{product.name}' успешно добавлен.")
            finally:
                print("Обработка добавления товара завершена.")
        else:
            raise TypeError()

    def middle_price(self) -> float:
        """Метод для подсчёта среднего ценника товара."""
        total = sum(product.price for product in self.__products)
        try:
            avg = total / len(self.__products)
        except ZeroDivisionError:
            return 0
        else:
            return round(avg, 2)

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
