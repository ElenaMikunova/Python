month = int(input("Введите месяц (числом): "))
my_dict = {"Зима":[1,2,12], "Весна":[3,4,5], "Лето":[6,7,8], "Осень":[9,10,11]}
for k, v in my_dict.items():
    if month in v:
        print(k)

# # решение только через список:
# month = int(input("Введите месяц: "))
# my_list = ["Зима", "Весна", "Лето", "Осень"]
# if 3<= month <= 5:
#     print(my_list[1])
# elif 6<= month <= 8:
#     print(my_list[2])
# elif 9<= month <= 11:
#     print(my_list[3])
# else:
#     print(my_list[0])

# Еще один вариант решения через список:
# month = int(input("Введите месяц: "))
# my_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
# print(my_list[month - 1])