from itertools import count, cycle


def func():
    for el in count(1, 2):
        if el > 20:
            break
        else:
            yield el


my_list = list(func())


def new_f():
    c = 0
    for x in cycle(my_list):
        if c > 15:
            break
        else:
            yield x
            c += 1


new_list = list(new_f())
print(my_list, new_list)
