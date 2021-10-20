new_f = open("text_3.txt", "r", encoding="utf-8")
my_list = sum(list(line.split() for line in new_f), [])
val_l = my_list[0::2]
key_l = list(map(float, my_list[1::2]))
my_d = dict(zip(key_l, val_l))
low_s = {v for k, v in my_d.items() if k < 20000}
print(f"Сотрудники с зарплатой менее 20000 рублей: {low_s}")
print(f"Средний размер дохода сотрудников: {sum(key_l) / len(key_l)} рублей.")
new_f.close()
