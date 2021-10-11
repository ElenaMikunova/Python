line = input("Введите слова (через пробел): ").split()
for index, value in enumerate(line):
    print(f"{index + 1}. {value[:10]}")