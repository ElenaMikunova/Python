def int_f():
    words = (input("Введите слова из маленьких латинских букв (через пробел): ")).split()
    all_chars = set("abcdefghigklmnopqrstuvwxyz")
    lat_w = list(filter(lambda el: set(el).issubset(all_chars), words))
    fin_list = [el.capitalize() for el in lat_w]
    return f"{fin_list}"


n = int_f()
print(n)
