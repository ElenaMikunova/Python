my_list = [1, 2, 3, 3, 3, 5, 76, 5, 5, 4, 101, 55, 4]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
