class Category:
    """Создает класс Категории и описываем его"""
    name: str
    description: str
    products: list
    def __init__(self, name, description, products, quantity_category=0, quantity_products=0):
        """Иницирует контструктор класса"""
        self.name = name
        self.description = description
        self.products = products
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
