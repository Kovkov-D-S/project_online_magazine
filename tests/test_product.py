# Импортируем фреймворк для тестирования кода
import pytest

# Импортируем класс объекта из файла product.py
from utils.product import Product


@pytest.fixture()
def example_product():
    return Product(name='Allples_Greene_Smith', description='kg', price=109.49, quantity=10)


def test_init(example_product):
    assert example_product.name == 'Allples_Greene_Smith'
    assert example_product.description == 'kg'
    assert example_product.price == 109.49
    assert example_product.quantity == 10