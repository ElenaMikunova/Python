class MyException(Exception):
    def __init__(self, text):
        self.text = text


num = input("Введите два числа через пробел: ")
try:
    my_list = list(map(int, num.split()))
    if len(my_list) != 2 or my_list[1] == 0:
        raise MyException("Делить на ноль нельзя!")
except (ValueError, MyException) as error:
    print(error)
else:
    print(f"{my_list[0] / my_list[1]}")
