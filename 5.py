vyr = int(input("Укажите выручку фирмы: "))
izd = int(input("Укажите издержки фирмы: "))
if vyr > izd:
    rent = (vyr - izd) / vyr * 100
    print(f"Вы получили прибыль!\nРентабельность выручки - {rent:.2f} %")
    sot = int(input("Укажите число сотрудников фирмы: "))
    pr_sot = (vyr - izd) / sot
    print(f"Прибыль фирмы в расчете на одного сотрудника: {pr_sot:.0f} руб.")
elif vyr < izd:
    ub = izd - vyr
    print(f"Вы терпите убытки!\nВаш убыток - {ub} руб.")
else:
    print("Вы достигли точки безубыточности!")
