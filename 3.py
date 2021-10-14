def my_func(ar_1, ar_2, ar_3):
    print(f"Сумма двух наибольших аргументов: {(sum([ar_1, ar_2, ar_3]) - min(ar_1, ar_2, ar_3))}")


my_func(
    float(input("Введите первое число: ")),
    float(input("Введите второе число: ")),
    float(input("Введите третье число: ")))
