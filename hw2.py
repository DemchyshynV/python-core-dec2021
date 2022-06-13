from typing import Callable


# def notebook() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list

    return (add_todo, get_all)


add_todo, get_all = notebook()

add_todo('go to home')
add_todo('go to work')


# print(get_all())


def expanded_form(n: int) -> str:
    nums = list(str(n))
    len_nums = len(nums) - 1
    return ' + '.join([item + '0' * (len_nums - i) for i, item in enumerate(nums) if item != '0']) + f' = {n}'


print(expanded_form(102301))


def decor(func):
    count = 1

    def inner(*args, **kwargs):
        nonlocal count
        print('count', count)
        func(*args, **kwargs)
        print('-------------------------------')
        count += 1

    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')




func1()
func2()
func1()
func1()
func2()
