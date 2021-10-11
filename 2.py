data = input("Введите элементы списка (через пробел): ").split()
if len(data) % 2 == 0:
    data[1::2], data[::2] = data[::2], data[1::2]
else:
    data[1:-1:2], data[:-1:2] = data[:-1:2], data[1:-1:2]
print(data)