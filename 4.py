number = int(input("Введите число: "))
max_n = 0
while number // 10 > 0:
    if number % 10 >= max_n:
        max_n = number % 10
    number = number // 10
if number % 10 >= max_n:
    max_n = number % 10
print("Самая большая цифра в числе - ", max_n)
