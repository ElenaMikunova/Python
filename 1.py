new_f = open("New file.txt", "x", encoding="utf-8")

while True:
    new_line = input("Введите информацию для записи (если закончили - нажмите Enter): ")
    if not new_line:
        break
    else:
        new_f.writelines(f"{new_line}\n")

new_f.close()
