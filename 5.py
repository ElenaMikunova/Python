exit_l = []
all_sum = []
while "q" not in exit_l:
    def my_f():
        my_list = (input("Введите числа через пробел (для остановки введите 'q'): ")).split()
        exit_l.extend(my_list)
        my_num = list(filter(lambda x: x.isdigit(), my_list))
        count_list = [int(el) for el in my_num]
        all_sum.extend(count_list)
        if my_list != my_num and "q" not in exit_l:
            print("Вводите только числа")
        return f"{sum(count_list)}({sum(all_sum)})"

    n = my_f()
    print(n)
    if "q" in exit_l:
        break
