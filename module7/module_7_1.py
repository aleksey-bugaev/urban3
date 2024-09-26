from pprint import pprint


class Product:
    """
    Атрибут name - название продукта (строка).
    Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
    Атрибут category - категория товара (строка).
    Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
    Все данные в строке разделены запятой с пробелами.
    """

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name} , {self.weight} , {self.category}"


class Shop:
    """
    Инкапсулированный атрибут __file_name = 'products.txt'.
    Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую
    строку со всеми товарами из файла __file_name.
    Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
    Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
    Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
    """
    __file_name = 'products.txt'

    def get_products(self):

        file = open(self.__file_name, 'r')
        str_file = file.read()
        file.close()
        return str_file

    def add(self, *products):

        str_write = ""
        file = open(self.__file_name, "r")
        # считываем все строки
        find_lines = file.read().splitlines()
        file.close()
        file = open(self.__file_name, "w")

        for a in products:
            for i in find_lines:
                if str(a) == i:
                    print(f"Продукт {i} уже есть в магазине")
                    continue
            str_write += str(a) + "\n"
        file.write(str_write)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
#
s1.add(p1, p2, p3)
#
print(s1.get_products())