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
        self.price = price
        self.quantity = quantity