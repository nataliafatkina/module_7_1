from unicodedata import category


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    from pprint import pprint

    __file_name = 'products.txt'

    def __init__(self):
        self.products = []

    def get_products(self):
        file = open(self.__file_name, 'r')
        list_file = file.readlines()
        str_file = ''.join(list_file)
        file.close()
        return str_file

    def add(self, *products):
        list_products = []
        result_products = []

        for product in products:
            list_products.append(str(product))
        print(list_products)

        file = open(self.__file_name, 'r+')
        list_file = [line.strip() for line in file.readlines()]
        print(list_file)
        for product in list_products:
            if product in list_file:
                result_products.append(f'Продукт {product} уже есть в магазине')
            else:
                file.write(product + '\n')
                result_products.append(product)
        str_result = '\n'.join(result_products)
        return print(str_result)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
