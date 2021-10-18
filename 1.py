from sys import argv

s_name, w_hour, h_rate, bonus = argv
try:
    int(w_hour), int(h_rate), int(bonus)
except ValueError:
    print("Введите только целочисленные значения")
else:
    print(f"Заработная плата: {int(w_hour) * int(h_rate) + int(bonus)}")
