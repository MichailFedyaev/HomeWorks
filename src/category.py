from src.product import Product

class Category:
    """Категория товара"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def add_product_str(self):
        product_str = ""
        for product in self.__products:
            product_str += f'{product.name}, {product.description} руб. Остаток: {product.quantity} шт.\n'
        return product_str

    @property
    def add_product_list(self):
        return self.__products
