my_list = [7, 5, 3, 3, 2]
num = int(input("Введите число: "))
for el in my_list:
    if num > el:
        my_list.insert(my_list.index(el), num)
        break
    elif num <= my_list[-1]:
        my_list.append(num)
        break
print(my_list)
