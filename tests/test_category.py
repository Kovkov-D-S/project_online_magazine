# Импортируем фреймворк для тестирования кода
import pytest

# Импортируем класс объекта из файла category.py
from utils.category import Category


@pytest.fixture()
def example_category():
    return Category(name = 'fruits', description = 'kg', products = ['apples', 'bananas', 'pineaplles'],
                    quantity_category = 1, quantity_products = 3)

def test_init(example_category):
    assert example_category.name == 'fruits'
    assert example_category.description == 'kg'
    assert example_category.products == ['apples', 'bananas', 'pineaplles']
    assert example_category.quantity_category == 1
    assert example_category.quantity_products == 3

def test_count_quantity_category(example_category):
    assert example_category.quantity_category == 1

def test_count_quantity_products(example_category):
    assert example_category.quantity_products == 3
