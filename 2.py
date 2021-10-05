time_sec = int(input("Введите время в секундах: "))
hour = time_sec // 3600
minute = time_sec % 3600 // 60
sec = time_sec % 3600 % 60
print(f"{hour:02}:{minute:02}:{sec:02}")
