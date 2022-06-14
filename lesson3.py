# class User:
#     count = 0
#
#
#
# user1 = User()
# user2 = User()
#
#
# print(user1.count)
#
# print(user2.count)
#
# User.count = 6
#
# print(user1.count)
#
# print(user2.count)


# class User:
#     def __init__(self, name, age):
#         self.age = age
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return self.__str__()
#
#     def get_name(self):
#         return self.name
#
#
# # user = User('Max', 18)
# #
# # # print(user.name)
# # # print(user.age)
# # print(user)
# #
# # print(user.get_name())
#
# users = [User('Max', 18), User('Kira', 20), User('Marina', 16)]
#
# print(users)


# class User:
#     def __init__(self, name):
#         self._name = name
#         # self._name = name
#
#     # def get_name(self):
#     #     return self.__name
#
#
# user = User('Max')
# print(user._User__name)
# print(user.get_name())


# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Greeting:
#     def greeting(self):
#         print('Hello')
#
#
# class UpUser(User, Greeting):
#     def __init__(self, name, age, status):
#         super().__init__(name, age)
#         self.status = status
#
#
# user = UpUser('Kira', 18, False)
#
# print(user.status)
# user.greeting()

# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def set_name(self, new_name):
#         self.__name = new_name
#
#     def get_name(self):
#         return self.__name
#
#     def delete_name(self):
#         del self.__name
#
#
# user = User('Max')
# print(user.get_name())
# user.set_name('Kira')
# print(user.get_name())
# user.delete_name()
# print(user.get_name())


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     def __set_name(self, new_name):
#         self.__name = new_name
#
#     def __get_name(self):
#         return self.__name
#
#     def __delete_name(self):
#         del self.__name
#
#     my_name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)


# user = User('Max')
# print(user.my_name)
# user.my_name = 'Kira'
# print(user.my_name)
# del user.my_name
# print(user.my_name)


# class User:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     # my_name = property(fget=__get_name, fset=__set_name, fdel=__delete_name)
#
#
# user = User('Max')
# print(user.name)
# user.name = 'Kira'
# print(user.name)
# del user.name
# print(user.name)

# class Shape:
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def area(self):
#         return self.a * self.b / 2 * self.c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def area(self):
#         return self.a * self.b
#
#     # def perimeter(self):
#     #     return self.a * self.b
#
#
# shapes: list[Shape] = [Triangle(1, 2, 3), Rectangle(1, 2), Triangle(3, 4, 5)]
#
# for shape in shapes:
#     print(shape.area())
#     print(shape.perimeter())

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Triangle(Shape):
#     def perimeter(self):
#         pass
#
#     def area(self):
#         pass
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# # shape = Shape()

# class User:
#     count = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # User.count += 1
#
#     def get_name(self):
#         print(self.name)
#
#     @staticmethod
#     def greeting():
#         print('Hello')
#
#     @classmethod
#     def inc_count(cls):
#         cls.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#
# User.greeting()
# print(User.get_count())
# User.inc_count()
# print(User.get_count())
# user = User('Max', 18)


# class User:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if not isinstance(cls.__instance, cls):
#             cls.__instance = super().__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#
# user1 = User('Max')
# user2 = User('Kira')
#
# print(user1)
# print(user2)
#
# print(user2 is user1)


# class Prod:
#     def __init__(self, value, name):
#         self.name = name
#         self.value = value
#
#     def __call__(self, num):
#         self.value *= num
#         return self.value
#
#
# prod = Prod(15, 'Max')
# print(prod.name)
# print(prod(5))
# print(prod.value)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.age + other.age

    def __sub__(self, other):
        return self.age - other.age

    def __mul__(self, other):
        return self.age * other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age


user1 = User('Max', 18)
user2 = User('Kira', 2)
# print(len(user1))

print(user1 + user2)
print(user1 - user2)
print(user1 * user2)
print(user1 < user2)
print(user1 > user2)
print(user1 == user2)
