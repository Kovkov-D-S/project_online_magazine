# Импортируем библиотеку json для преобразования данных в список
import json

# Строим пути к файлам с учетом особенностей ОС.
import os

# Импортируем класс объекта из файла category.py
from utils.category import Category

# Импортируем класс объекта из файла product.py
from utils.product import Product


ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
file_products = os.path.join(ROOT_PATH, 'src', 'products.json')

def load_products_list():
    """Загружает список категорий и продуктов из файла "products.json" и возвращает экземпляры классов."""
    with open(file_products, 'r', encoding="utf-8") as file:
        categoryes_list = json.loads(file.read())
        for categoryes in categoryes_list:
            products_list = categoryes['products']
            for products in products_list:
                return Product(name=products['name'], description=products['description'],
                                   price=products['price'], quantity=products['quantity'])

            return Category(name=categoryes['name'], description=categoryes['description'],
                            products=categoryes['products'])

