a = int(input("Укажите, сколько километров Вы пробежали в первый день: "))
b = int(input("Укажите, сколько километров Вы хотите пробежать: "))
count = 1
while a < b:
    a = a * 1.1
    count += 1
print(count)
