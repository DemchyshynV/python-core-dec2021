# l = [1, 2, 3, 4]
#
# # print(next(l))
# # print(dir(l))
# i = iter(l)
#
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

class MyRange:
    def __init__(self, length):
        self.__length = length
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__length:
            res = self.__counter
            self.__counter += 1
            return res
        raise StopIteration


def my_range2(length):
    count = 0
    while count < length:
        yield count
        count += 1


my_range = MyRange(3)

# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))

l = [1, 2, 3]

for i in my_range2(6):
    print(i)
