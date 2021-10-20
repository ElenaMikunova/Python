with open("New_5.txt", "x+", encoding="utf-8") as new_f:
    my_num = input("Введите числа, разделенные пробелами: ")
    try:
        try_list = list(map(int, my_num.split()))
    except ValueError:
        print("Вводите только числа!")
    else:
        num_list = my_num
        new_f.writelines(f"{num_list}\n")
    new_f.seek(0)
    f_read = sum(map(int, new_f.read().split()))
    print(f"Сумма чисел в файле: {f_read}")
