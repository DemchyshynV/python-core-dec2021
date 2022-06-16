# a = 0
# for i in range(10):
#     a += i
#     print(a)

# class MyException(Exception):
#     pass
#
# try:
#     # khdgsfsjf
#     # print(44/0)
#     raise MyException
# except NameError as err:
#     print(err)
# # except ZeroDivisionError as err:
# #     print(err)
# except MyException:
#     print('my')
# except Exception as err:
#     print(err)
# else:
#     print('all right')
# finally:
#     print('finish')
#
# print('sdfsdf')

# l = [i for i in range(50000000)]
# input()

# g = (i for i in range(50000000))
# input()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# for i in g:
#     print(i)


# g = (i for i in range(5))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
#
# for i in g:
#     print(i)


# def gen(name):
#     for ch in name:
#         yield ch
#         print('print')
#
#
# g = gen('Max')
#
# print(next(g))
# print(next(g))
# # print(next(g))


# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'return'
#
#
# g = gen()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen1(n):
#     for i in range(n):
#         yield f'{i}-Team1'
#
#
# def gen2(n):
#     for i in range(n):
#         yield f'{i}-Team2'
#
#
# teams = [gen1(8), gen2(5)]
#
# while teams:
#     team = teams.pop(0)
#     try:
#         print(next(team))
#         teams.append(team)
#     except StopIteration:
#         pass

# import uuid
#
# def gen_jpg_file_name():
#     pattern = '{}.jpg'
#     while True:
#         yield pattern.format(uuid.uuid1())
#
#
# gen = gen_jpg_file_name()
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# # try:
# #     file = open('11.txt', 'w')
# #     try:
# #         # print(file.read())
# #         # file.write('sssssss')
# #         # print(file.read(2))
# #         # print([file.readline()])
# #         # print([file.readline()])
# #         # print([file.readline()])
# #         # print([file.readline()])
# #         # print([file.readline()])
# #         # print(file.readlines())
# #         # for line in file.readlines():
# #         #     print(line)
# #         print('Hello', file=file)
# #     finally:
# #         file.close()
# # except FileNotFoundError as err:
# #     print(err)
# # except Exception as err:
# #     print(err)
# try:
#     with open('11.txt') as file:
#         print(file.read())
# except Exception as err:
#     print(err)


# try:
#     with open('123.png', 'rb') as file:
#         with open('my.png', 'wb') as file2:
#             file2.write(file.read())
# except Exception as err:
#     print(err)


import pickle


# user = {
#     'name': 'Max',
#     'age': 15
# }

# try:
#     with open('myusers', 'wb') as file:
#         pickle.dump(user, file)
# except Exception:
#     pass


# try:
#     with open('myusers', 'rb') as file:
#         user = pickle.load(file)
#         print(user)
# except Exception:
#     pass


# user = {
#     'name': 'Max',
#     'age': 15
# }
#
# import json
#
# try:
#     with open('myuser.json', 'w') as file:
#         json.dump(user, file)
# except Exception:
#     pass
#
#
# try:
#     with open('myuser.json', 'r') as file:
#         user = json.load(file)
#         print(user)
# except Exception:
#     pass


# p = 45
#
# match p:
#     case 1:
#         print('1')
#     case 2:
#         print('2')
#     case _:
#         print('Not Found')

# a = ['top', 200]
#
# match a:
#     case 'left' | 'top' as action, value:
#         print(f'{action=}', value)
#     case action, value:
#         print(action, value)
#     case _:
#         print('Not Found')


# user = {
#     'name': 'Max',
#     'age': 15
# }
#
# match user:
#     case {'name': 'Max' | 'Kira' as name, 'age': int(age)}:
#         print(f'{name=} {age=}')
#     case _:
#         print('Not Found')


class User:
    __match_args__ = 'name', 'age'

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Ma15', 15)

user2 = {
    'name': 11,
    'age': 15
}


def matcher(data: User | dict):
    match data:
        case User('Max' as name):
            print(name)
        case {'name': str(name)}:
            print(name)

matcher(user2)
