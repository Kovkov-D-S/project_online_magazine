# from category import Category

class Product:
    """Создает класс Продукты и описываем его"""
    name: str
    description: str
    price: float
    quantity: int
    def __init__(self, name, description, price, quantity):
        """Иницирует контструктор класса"""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def add_object_product(cls, name, description, price, quantity):
        """Создает товар как объект класса и возвращается его"""
        return cls(name, description, price, quantity)

    def check_add_object_product(self, list_products):
        """Проверяем поступивший товар на уникальность с существующим и при уникальности добавляем его в список товаров."""
        for product in list_products:
            if product.name == self.name:
                product.quantity += self.quantity
                if self.price > product.price:
                    product.price = self.price


    @property
    def price(self):
        """Геттер цены товара. Предоставляет доступ к отрибуту для изменения его значения."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Сеттер цены товаров. Изменяем значения атрибута."""
        if new_price <= 0:
            print("Введена некорректная цена")
        elif new_price > self._price:
            self._price = new_price
        else:
            while True:
                user_answer = input('Новая цена ниже текущей. Вы подтверждаете понижение цены? (y/n)\n')
                if user_answer == 'y':
                    self._price = new_price
                    print('Цена обновлена!')
                    break
                elif user_answer == 'n':
                    print('Цена не изменена.')
                else:
                    print('Введите корректный ответ!')

    def __repr__(self):
        """Выводим общую информацию о классе."""
        return f'Product {self.name}, {self.description}, {self.price}, {self.quantity}'