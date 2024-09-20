class Vehicle:
    """
    Атрибут owner(str) - владелец транспорта.(владелец может меняться)
    Атрибут __model(str) - модель(марка) транспорта.(мы не можем менять название модели)
    Атрибут __engine_power(int) - мощность двигателя.(мы не можем менять мощность двигателя самостоятельно)
    Атрибут __color(str) - название цвета.(мы не можем менять цвет автомобиля своими руками)
    Атрибут __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания.

    Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
        а так же владельца в конце в формате "Владелец: <имя>"
    Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
        если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
        "Нельзя сменить цвет на <новый цвет>".
     """

    # owner = ""
    # __model = ""
    # __engine_power = 0
    # __color = ""
    # __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner="", model="", color="", engine_power=0):
        self.owner = owner
        self.__model = model
        self.__color = color
        self.__engine_power = engine_power
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        ##список и новый цвет в нижний регистр
        u_list = []
        u_list = list(map(str.upper, self.__COLOR_VARIANTS))

        u_color = new_color.upper()
        if u_color in u_list:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}.")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
#
#
# # Изначальные свойства
vehicle1.print_info()
#
# # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
#
# # Проверяем что поменялось
vehicle1.print_info()
