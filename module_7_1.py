class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().strip().split('\n')
        existing_products_set = {product.split(',')[0] for product in existing_products if product}

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in existing_products_set:
                    print(f"Продукт {product} уже есть в магазине")
                else:
                    file.write(str(product) + '\n')

# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Вывод str для проверки
print(p2)  # Spaghetti, 3.4, Groceries

# Добавление продуктов в магазин
s1.add(p1, p2, p3)

# Вывод продуктов из магазина
print(s1.get_products())
