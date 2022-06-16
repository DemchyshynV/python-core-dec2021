# Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__area = y * x

    def __add__(self, other):
        return self.__area + other.__area

    def __sub__(self, other):
        return self.__area - other.__area

    def __eq__(self, other):
        return self.__area == other.__area

    def __ne__(self, other):
        return self.__area != other.__area

    def __gt__(self, other):
        return self.__area > other.__area

    def __lt__(self, other):
        return self.__area < other.__area

    def __len__(self):
        return self.x + self.y


rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(6, 8)

print(rectangle1 + rectangle2)
print(rectangle1 - rectangle2)
print(rectangle1 == rectangle2)
print(rectangle1 < rectangle2)
print(rectangle1 > rectangle2)
print(len(rectangle1))


#   ###############################################################################
#
# создать класс Human (name, age)
# создать два класса Prince и Cinderella:
# у золушки должно быть имя возраст и размер ноги
# у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую
#
# в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
# и метод класса который будет показывать это количество


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    def __str__(self):
        return str(self.__dict__)


class Prince(Human):
    def __init__(self, name, age, find_size):
        super().__init__(name, age)
        self.find_size = find_size

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if self.find_size == cinderella.foot_size:
                print(cinderella)
                return
        print('Not Found')


cinderellas_list =[
    Cinderella('Kira', 18, 20),
    Cinderella('Marina', 16, 21),
    Cinderella('Olha', 20, 30),
    Cinderella('Kamila', 12, 12),
    Cinderella('Lisa', 18, 36),
]

prince = Prince('Kokos', 5, 38)

prince.find_cinderella(cinderellas_list)
