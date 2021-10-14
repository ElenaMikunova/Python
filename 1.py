def my_f(arg_1, arg_2):
    try:
        div = arg_1 / arg_2
    except ZeroDivisionError:
        print("Мы не делим на ноль.")
    else:
        print(f"Результат деления: {div:.02}")


my_f(float(input("Введите первое число: ")), float(input("Введите второе число: ")))

