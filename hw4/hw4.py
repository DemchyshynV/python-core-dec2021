"""
задача записать в новый текстовый файл только почты от gmail.com
"""
# FILE = 'emails.txt'
# RES_FILE = 'res_emails.txt'
# #
# try:
#     with open(FILE) as file, open(RES_FILE, 'a') as res_file:
#         for line in file:
#             email = line.split()[-1]
#             if email.endswith('@gmail.com'):
#                 # print(email, file=res_file)
#                 res_file.write(f'{email}\n')
# except Exception as err:
#     print(err)
"""
реализовать записную книжку покупок:
- каждая запись должна содержать название покупки и ее цену
-сделать менюшку для работы с записной книжкой:
    '1) Создать запись'
    '2) Список все записей'
    '3) Общая сумма всех покупок'
    '4) Самая дорогая покупка'
    '5) Поиск по названию покупки'
    '9) Выход'
- можете придумать свои пункты
"""
import json
from typing import TypedDict

NoteType = TypedDict('NoteType', {'purchase': str, 'cost': int})


class Note:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__notes: list[NoteType] = []
        try:
            with open(file_name) as file:
                self.__notes: list[NoteType] = json.load(file)
        except:
            pass

    def add(self):
        try:
            with open(self.__file_name, 'w') as file:
                purchase = input('Введіть назву покупки: ')
                cost = ''

                while not cost.isdigit():
                    cost = input('Введіть ціну покупки: ')

                self.__notes.append({'purchase': purchase, 'cost': int(cost)})
                json.dump(self.__notes, file)
        except:
            print('Щось пішло не так!!!')

    def show_all(self):
        if not self.__notes:
            print('В вас немає записів!!!')
            return

        for item in self.__notes:
            print(item)

    def sum_of_costs(self):
        sum_costs = sum(item['cost'] for item in self.__notes)
        print(f'{sum_costs=}')

    def most_expensive(self):
        print(max(self.__notes, key=lambda item: item['cost']))

    def find_by_name(self):
        find = input('Введіть назву покупки')
        for item in self.__notes:
            if item['purchase'].lower() == find.lower():
                print(item)
                return

        print('Не знайдено!!!')


note = Note('purchases.json')

while True:
    print('1) Создать запись')
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('9) Выход')

    choice = input('Зробіть ваш вибір: ')

    match choice:
        case '1':
            note.add()
        case '2':
            note.show_all()
        case '3':
            note.sum_of_costs()
        case '4':
            note.most_expensive()
        case '5':
            note.find_by_name()
        case '9':
            break
