from functools import reduce
my_list = [el for el in range(100, 1001, 2)]


def my_func(n, m):
    return n * m


print(reduce(my_func, my_list))
