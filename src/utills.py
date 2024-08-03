import json
import os
from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    """Читает JSON-файл и преобразует его в список словарей"""
    full_path = os.path.abspath(path)
    with open(path, 'r', encoding='UTF-8') as file:
        result = json.load(file)
    return result


def create_json(data):
    """Создаёт объекты из полученных данных"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category_obj = Category(category["name"], category["description"], products)
        categories.append(category_obj)
    return categories


if __name__ == "__main__":
    files = read_json("..//data/products.json")
    users_data = create_json(files)
    print(files)
    print(users_data)