quest = input("Хотите ли вы ввести новый товар? (Ответьте да / нет): ")
n = 0
item_list = []
name_list = []
price_list = []
count_list = []
unit_list = []
while quest == "да":
    n = n + 1
    name = input("Введите название товара: ")
    name_list.insert(0, name)
    price = int(input("Введите цену товара (числом): "))
    price_list.insert(0, price)
    count = int(input("Введите количество товара (числом): "))
    count_list.insert(0, count)
    unit = input("Введите единицу измерения товара: ")
    unit_list.insert(0, unit)
    item_dict = {"название": name, "цена": price, "количество": count, "единицы измерения": unit}
    item_t = (n, item_dict)
    item_list.append(item_t)
    quest = input("Хотите ли вы ввести новый товар? (Ответьте да / нет): ")
if quest == "нет":
    print(*item_list, sep="\n")
analit = input("Вы хотите собрать аналитику о товарах? (Ответьте да / нет): ")
if analit == "нет":
    print("До свидания!")
if analit == "да":
    analit_dict = {"Название": name_list, "Цена": price_list, "Количество": count_list, "Ед.": unit_list}
    print(*analit_dict.items(), sep="\n")