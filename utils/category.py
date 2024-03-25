from product import Product

class Category:
    """Создает класс Категории и описываем его"""
    name: str
    description: str
    products: list
    def __init__(self, name, description, products, quantity_category=0, quantity_products=0):
        """Иницирует контструктор класса"""
        self.name = name
        self.description = description
        self.__products = products
        self.quantity_category = quantity_category
        self.quantity_products = quantity_products
    def count_quantity_category(self):
        """Считает общее количество категорий товаров"""
        self.quantity_category += self.quantity_category
        return self.quantity_category
    def count_quantity_products(self):
        """Считает общее количество уникальных продуктов"""
        self.quantity_products += len(products)
        return self.quantity_products

    @property
    def products(self):
        """Геттер списка товаров. Предоставляет доступ к отрибуту для изменения его значения."""
        return self.__products

    @products.setter
    def products(self, instance_product):
        """Сеттер списка товаров. Изменяем значения атрибута."""
        instance_product
        print(instance_product)
        if isinstance(instance_product, self.__class__):
            return self.__products.append(instance_product)

    @property
    def formated_product(self):
        """Геттер списка товаров. Выводим данные из списка товаров в необходимый вид."""
        for product in self.__products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."

    def __repr__(self):
        """Выводим общую информацию о классе."""
        return f'Category {self.name}, {self.description}, {self.products}'


instance_product_1 = Product.add_object_product(name='Gorizont', description='55 дюймов', price=138000.0, quantity=5)

instance_product_2 = Product.add_object_product(name='55\" QLED 4K', description='Фоновая подсветка', price=135000.0, quantity=5)
instance_product_3 = Product.add_object_product(name='Gorizont', description='55 дюймов', price=133000.0, quantity=5)
category_1 = Category(name="Телевизоры",
    description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    products=[Product(name='55\" QLED 4K', description='Фоновая подсветка', price=123000.0, quantity=7)])
# print(category_1)
# print(instance_product_1)
# instance_product_1.check_add_object_product(category_1.products)
# print(category_1.products)
# print(instance_product_2)
# instance_product_2.check_add_object_product(category_1.products)
# print(category_1.products)
# print(instance_product_3)
# instance_product_3.check_add_object_product(category_1.products)
# print(category_1.products)