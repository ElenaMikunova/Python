class MyException(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    num = input("Введите число: ")
    if num == "stop":
        break
    else:
        try:
            num.isdigit()
            if num.isdigit() is False:
                raise MyException("Вводите только числа!")
        except MyException as error:
            print(error)
        else:
            my_list.append(int(num))

print(my_list)
