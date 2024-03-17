# Импортируем фреймворк для тестирования кода
import pytest

# Импортируем класс объекта из файла category.py
from utils.func import load_products_list

# Импортируем класс объекта из файла category.py
from utils.category import Category

# Импортируем класс объекта из файла category.py
from utils.product import Product

@pytest.fixture
def test_products_list():
    return [{"name": "Телевизоры",
    "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    "products": [{"name": "55\" QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}]}]

@pytest.fixture
def test_products_list_file(tmpdir, test_products_list):
    file_path = os.path.join(tmpdir, 'products.json')
    with open(file_path, 'w') as f:
        json.dump(test_products_list, f)
    return file_path

@pytest.fixture
def test_return_class_category():
    return Category(name='Телевизоры', description='Современный телевизор, который позволяет наслаждаться просмотром, '
                                                   'станет вашим другом и помощником',
                            products=[{"name": "55\" QLED 4K", "description": "Фоновая подсветка",
                                       "price": 123000.0, "quantity": 7}]), Product(name='55\" QLED 4K', description='Фоновая подсветка',
                               price=123000.0, quantity=7)

@pytest.fixture
def test_return_class_category():
    return Category(name='Телевизоры', description='Современный телевизор, который позволяет наслаждаться просмотром, '
                                                   'станет вашим другом и помощником',
                            products=[{"name": "55\" QLED 4K", "description": "Фоновая подсветка",
                                       "price": 123000.0, "quantity": 7}])


@pytest.fixture
def test_return_class_product():
    return Product(name='55\" QLED 4K', description='Фоновая подсветка', price=123000.0, quantity=7)

def test_load_products_list(test_products_list, test_return_class_category, test_return_class_product):
    test_return_classes_categoryes = test_return_class_category
    test_return_classes_products = test_return_class_product
    for categoryes in test_products_list:
        products_list = categoryes['products']
        # assert test_example_instance_category == test_return_classes()
        for products in products_list:
            test_example_instance_product = Product(name=products['name'], description=products['description'],
                               price=products['price'], quantity=products['quantity'])
            # test_example_tuple = test_example_instance_category, test_example_instance_product
            assert test_example_instance_product.name == test_return_class_product.name
            assert test_example_instance_product.description == test_return_class_product.description
            assert test_example_instance_product.price == test_return_class_product.price
            assert test_example_instance_product.quantity == test_return_class_product.quantity
        test_example_instance_category = Category(name=categoryes['name'],
                                                  description=categoryes['description'],
                                                  products=categoryes['products'])
        assert test_example_instance_category.name == test_return_class_category.name
        assert test_example_instance_category.description == test_return_class_category.description
        assert test_example_instance_category.products == test_return_class_category.products