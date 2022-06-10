# l = ['a', 'b', 'c']
#
# # for i in range(len(l)):
# #     print(l[i])
#
# for i,v in enumerate(l):
#     print(i)
#     print(v)

# tuple1 = (1, 2)
#
# a,b = tuple1
#
# print(a)
# print(b)

# a = 5
# b = 10
#
# b,a = (a, b)
#
# print(a)
# print(b)

# l = [1, 2, 3, 4, 5]
#
# # a, b, _, d, *_ = l
# #
# # print(a, b, d)
# print(*l)

#
# user = {
#     'name': 'Max',
#     'age': 15
# }
#
#
# def func(name, age):
#     return name, age
#
# #
# # print(func(**user))
#
# user = {
#     'name': 'Max',
#     'age': 15
# }
#
# user = {**user, 'status':True}
#
# print(user)
#
# l = [1,2,3]
#
# l = [*l, 4,5,6]
# print(l)
#

# decorators


#
# def decor(func):
#     def inner(*args, **kwargs):
#         print('***************************')
#         func(*args, **kwargs)
#         print('***************************')
#
#     return inner
#
# @decor
# def greeting(name):
#     print(f'Hello, {name}')
#
# @decor
# @decor
# def greeting2(name, age):
#     print(f'Hello, {name}, I`m {age}')
#
#
# greeting('Max')
# greeting2('Kira', 18)
# # start = decor(greeting)
# # start2 = decor(greeting2)
# # # start = decor(start)
# #
# # start('Max')
# #
# # start2('name', 15)


# Scope


# name = 'MAx'
#
#
# def func():
#     name = 'Kira'
#     print(locals())
#
#
# func()
#
#
# for i in range(10):
#     pass
#
#
# print(globals())


# name = 'Max'
#
#
# def a():
#     name = 'Vasia'
#
#     def b():
#         global name
#         name = 'Kira'
#         print(name)
#
#     b()
#     print(name)
#
#
# a()
# print(name)

# closure
#
# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#
#     return inner
#
#
# count1 = counter()
# count2 = counter()
#
# print(count1())
# print(count1())
#
# print(count2())
#
# print(count1())
# print(count1())
#
# print(count2())
#
# # lambda
#

# const func =(x,y)=>x+y
#
# func = lambda x, y: x + y
#
# print(func(2, 6))

# l = [1, 2, 3, 4, 5, 6]
#
# # l.map(value=>value+value)
# m = map(lambda value: value + value, l)

# for i in m:
#     print(i)
#
# for i in m:
#     print(i)

# print(list(m))
# print(list(m))


# def func(s: str) -> int:
#     return 'hhh'
#
#
# print(func(1123))

from typing import Callable, List, Tuple, Optional, Union, NewType, Any, Dict, TypedDict

# # def func(st: str, a: int, status: bool) -> Optional[str]:
# # def func(st: str, a: int, status: bool) -> Union[str, int, None]:
# # def func(st: str, a: int, status: bool) -> str | None:
# def func(st: str, a: int, status: bool) -> str | int | None:
#     return None
#     # return None
#     # return None

l: list[str] = [1, 2, '3']

t: tuple[str, ...] = ('1',)

# d: dict[str, str] = {'name': 'ssss', 'age': 1}


User = TypedDict('User', {'name': str, 'age': int, 'status': bool}, total=False)

user: User = {'name': 'Max', 'status': True, 'sss': 33}

UserId = NewType('UserId', int)


# def func(user_id: UserId):
#     pass
#
#
# user_id = UserId(22)
#
# func(user_id)


def counter() -> Callable[[int, str], int]:
    count = 0

    def inner(a: int, b: str) -> int:
        nonlocal count
        count += 1
        return count

    return inner


func = counter()
func()
