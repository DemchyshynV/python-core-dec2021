# kjsdfkjshfkjsfhsjk

'''
kshdfkjshf
sjhdfkjshfkjsdf
jhsdfjkshjdkf
'''

"""
kjhskjhfksdf
jsldhfkjsdf
"""
# print(1, 2, 3, sep='', end='Finish\n')
#
# i = 3
# f = 1.2
# b = True # False
# n = None
#
# print(type(i))
# print(type(f))
# print(type(b))
# print(type(n))
#
# print(type(float(i)))

# a = b = c = 10
# print(a, b, c)
# a = 5
# b = 2

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(round(2.6))
# print(int(2.8+0.5))
# print(a%b)
# print(a**b)

# print(2525**2525)

# s = input('Enter num: ')
#
# print('input', s)
# a = 5
# b = 2
# print(a < b)
# print(a > b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)
# print(not True)
#
# print(isinstance(1.6, float))
# num = int(input('num: '))
# if (5 <= num <= 7) or num==15:
#     print(True)
# elif num == 8:
#     print(8)
# else:
#     print('some')


# res = 'yes' if num > 5 else 'no'
#
# print(res)


# list

# l = [1, 2, 3, 4, 5, 7]
# a = l.copy()
# print(l[34])
# print(l[-25])
# l[0]= 555
# del l[3]
# print(len(l))
# print(l)
# print(a)
#
# print(a == l)
# print(a is not l)


# a = [1, 2, 3, 4, 5, 6, 2]
# a.append(5)
# a.insert(1, 555)
# pop = a.pop()
# pop = a.pop(4)
# a.remove(2)
# a.extend([3,4,5,6])
# a += [3, 4, 5]
# print(a.index(2, 3, 88))

# a.reverse()
# a.sort(reverse=True)
# print(a.count(55))
# a.clear()
# print(a)

# b = 0
#
# b = 1


# a = [1, 2, 3, 4, 5, 6, 2]
#
# l = a[::2]
# print(l)

# list()


# tuple


# my_tuple = (1, 2, 3, 4, 5)
#
# # print(my_tuple.count(2))
# # print(my_tuple.index(2))
#
# # my_tuple[0] = 4
# l = list(my_tuple)
# print(l)


# dictionary

# dict()


# t = tuple([1, 2, 3, 4, 5, 7])
# # print(t)
#
# # d = dict(name='max', age=15)
# d = {True: 'max'}
# print(d)


# user = {
#     'name': 'Max',
#     'age': 15,
#     'gender': 'male'
# }

# print(user['name'])
# print(user.get('name1', 555))
# user['name_a'] = 'Kira'

# print(user)

# copy = user.copy()
# print(user.items())
# print(list(user.keys())[0])
# pop = user.pop('age2', None)
# print(pop)
# popitem = user.popitem()
# user.update({'status':True})
# user.update(status=True)
# user |={'status':False}
# print(user.values())


# user = {
#     'name': 'Max',
#     'age': 15,
#     'gender': 'male'
# }

# setdefault_value = user.setdefault('key', 'my_key')
# setdefault_value = user.setdefault('age', 'my_key')
# print(setdefault_value)
# print(user)

# d = {}

# print(type(d))
# l = [1, 2, 3, 4, 6, 2, 5, 4]
#
# s = set(l)
# s = set()
#
# s.add(3)
# s.add(2)
# s.add(4)
# s.add(1)
# pop = s.pop()
# print(pop)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {10, 9, 3, 7}

# print(set1.issuperset(set2))
# print(set2.issubset(set1))
# print(set1.isdisjoint(set2))
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# set1.remove(2)
# set1.discard(2222)
#
# print(set1)


# string


# string = 'sjhfdgsjd'
# string = "sjhfdgsjd"
#
# # string = """
# # sdjfhskjhf
# # sdkfhksjhf
# # sjdhfkjsdhf
# # """

# print(string)

# name = 'Max'
# age = 18
# weight = 70.5
#
# string = 'Hello, my name is Max, I`m 18 and my weight 70.5 kg'
# string = 'Hello, my name is ' + name + ', I`m ' + str(age) + ' and my weight ' + str(weight) + ' kg'
# string = 'Hello, my name is %s, I`m %i and my weight %f kg' % (name, age, weight)
# string = 'Hello, my name is {}, I`m {} and my weight {} kg'.format(name, age, weight)
# string = 'Hello, my name is {name}, I`m {age} and my weight {weight} kg'.format(age=age,name=name, weight=weight)
# string = f'Hello, my name is {name}, I`m {age} and my weight {weight} kg'
#
# print(string)
#
#
# print('hello worlds'.title())
# print('Hello Worlds'.swapcase())
# print('Hello1Worlds'.isalpha())
# print('1111'.isdigit())
# print('Hello122Worlds'.isalnum())
#
# print('hello worlds'.startswith('ll'))
# print('hello worlds'.endswith('s'))
#
# print(['aaa   sdd     aaa'.strip('a d')])
# print(['aaa   sdd     aaa'.rstrip('a')])
# print(['aaa   sdd     aaa'.lstrip('a')])
# print('a-b-c-d'.split('-'))
# print('hello is hello'.partition('is'))
# print('-'.join('hello is hello'.partition('is')))
#
# # print('hello'[0])

# print(min(1, 2, 3, 4, 5, 6, 7, -3))
# print(max([1, 2, 3, 4, 5, 6, 7, -3]))
#
# l = [2,5,2,5,7,3]
# sorted1 = sorted(l, reverse=True)
# print(pow(2, 8))
# print(2**8)
# print(l)
# print(sorted1)


# def some_func(a, b, c=222, *args, **kwargs):
#     print('hello', a, b)
#     print(args)
#     print(kwargs)
#     return c
#
#
# func = some_func(4, 6, 55, 5,6,7,8,9, name='Max')
#
# print(func)

# i = 5
# while i > 0:
#     print(i)
#     i -= 1
# else:
#     print('finish')
#
# l = [1, 2, 3, 5, 2, 3, 5, 3, 5, 7]

# print(4 in [2, 3, 6, 3])

# for i in l:
#     print(i)

# for i in range(1, 100, 3):
#     print(i)

user = {
    'name': 'Max',
    'age': 15,
    'gender': 'male'
}

# for k, v in user.items():
#     print('key', k)
#     print('value', v)


# list comprehension

# l1 = [i for i in range(10)]
# print(l1)

# ll = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ]

# # l = [i for j in ll for i in j]
#
# l = []
#
# for j in ll:
#     for i in j:
#         l.append(i)

l = [1, 2, 3, 4, 5, 7]

# res = [i for i in l if i > 3]
# res = [i**2 for i in l]
# res = [i ** 2 for i in l if i > 4]
res = [i ** 2 if i > 4 else i ** 3 for i in l]
print(res)
