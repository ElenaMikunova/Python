new_f = open("New_4.txt", "x", encoding="utf-8")
with open("text_4.txt", "r+", encoding="utf-8") as start_f:

    while True:
        content = start_f.readline()
        if not content:
            break
        else:
            my_str = content.replace("One", "Один").\
                replace("Two", "Два").\
                replace("Three", "Три").\
                replace("Four", "Четыре")
            print(my_str)
            new_f.writelines(f"{my_str}\n")

new_f.close()
