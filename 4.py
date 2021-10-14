"""Оптимальное решение"""


def my_f(x, y):
    print(pow(x, y))


my_f(
    float(input("Введите действительное положительное число: ")),
    int(input("Введите целое отрицательное число: ")))


"""Решение через цикл"""


# def my_f(x, y):
#     n = 0
#     count_x = []
#     res = 1
#     while n < abs(y):
#         n += 1
#         count_x.append(x)
#     for el in count_x:
#         res *= el
#     print(1 / res)
#
#
# my_f(float(input("Введите действительное положительное число: ")), int(input("Введите целое отрицательное число: ")))
