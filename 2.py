def my_f(name, e_mail, phone, sur, dob, city):
    print(f"{sur} {name}, д.р. {dob}. Город: {city}. Контакты: {phone}, {e_mail}")


my_f(
    name=input("Имя: "),
    sur=input("Фамилия: "),
    dob=input("Дата рождения: "),
    city=input("Город проживания: "),
    phone=input("Номер телефона: "),
    e_mail=input("E-mail: ")
)

"""Еще вариант через словарь"""
# def my_f(**kwargs):
#     print(kwargs)
#
#
# my_f(
#     name=input("Имя: "),
#     sur=input("Фамилия: "),
#     dob=input("Дата рождения: "),
#     city=input("Город проживания: "),
#     phone=input("Номер телефона: "),
#     e_mail=input("E-mail: ")
# )
