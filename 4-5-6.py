from abc import abstractmethod


class Warehouse:
    scanners = []
    printers = []
    xeroxes = []
    shop = []

    @staticmethod
    def my_scan():
        if len(Warehouse.scanners) == 0:
            print("На складе нет сканнеров.")
        else:
            print("На складе есть сканеры: ")
            for n, el in enumerate(Warehouse.scanners):
                print(f"{n + 1}. {el[0]} {el[1]}, стоимость - {el[2]} руб.")

    @staticmethod
    def my_print():
        if len(Warehouse.printers) == 0:
            print("На складе нет принтеров.")
        else:
            print("На складе есть принтеры: ")
            for n, el in enumerate(Warehouse.printers):
                print(f"{n + 1}. {el[0]} {el[1]}, стоимость - {el[2]} руб.")

    @staticmethod
    def my_xerox():
        if len(Warehouse.xeroxes) == 0:
            print("На складе нет ксероксов.")
        else:
            print("На складе есть ксероксы: ")
            for n, el in enumerate(Warehouse.xeroxes):
                print(f"{n + 1}. {el[0]} {el[1]}, стоимость - {el[2]} руб.")

    @staticmethod
    def all_count():
        my_sum = sum([sum(el[2] for el in Warehouse.scanners),
                      sum(el[2] for el in Warehouse.printers),
                      sum(el[2] for el in Warehouse.xeroxes)])
        print(f"Общая стоимость товаров на складе - {my_sum} руб.")

    @staticmethod
    def to_shop1():
        n = int(scan_num) - 1
        Warehouse.shop.append(Warehouse.scanners[n])
        Warehouse.scanners.remove(Warehouse.scanners[n])

    @staticmethod
    def to_shop2():
        n = int(print_num) - 1
        Warehouse.shop.append(Warehouse.printers[n])
        Warehouse.printers.remove(Warehouse.printers[n])

    @staticmethod
    def to_shop3():
        n = int(xerox_num) - 1
        Warehouse.shop.append(Warehouse.xeroxes[n])
        Warehouse.xeroxes.remove(Warehouse.xeroxes[n])

    @staticmethod
    def my_shop():
        if len(Warehouse.shop) == 0:
            print("В магазине нет товаров.")
        else:
            print("В магазине есть следующие товары:")
            for n, el in enumerate(Warehouse.shop):
                print(f"{n + 1}. {el[0]} {el[1]}, стоимость - {el[2]} руб.")


class OfficeEq:
    @abstractmethod
    def __init__(self, my_name, my_model, my_price):
        self.my_name = my_name
        self.my_model = my_model
        self.my_price = my_price

    @abstractmethod
    def to_ware(self):
        pass


class Scanner(OfficeEq):
    def __init__(self, my_name, my_model, my_price):
        super().__init__(my_name, my_model, my_price)

    def to_ware(self, *scan):
        Warehouse().scanners.append([self.my_name, self.my_model, self.my_price])


class Printer(OfficeEq):
    def __init__(self, my_name, my_model, my_price):
        super().__init__(my_name, my_model, my_price)

    def to_ware(self, *printer):
        Warehouse().printers.append([self.my_name, self.my_model, self.my_price])


class Xerox(OfficeEq):
    def __init__(self, my_name, my_model, my_price):
        super().__init__(my_name, my_model, my_price)

    def to_ware(self, *xerox):
        Warehouse().xeroxes.append([self.my_name, self.my_model, self.my_price])


scan_1 = Scanner("HP", "ScanJet 40", 60000)
scan_2 = Scanner("Epson", "DS-1630", 29000)
scan_3 = Scanner("PlusTech", "SmartOffice", 27000)
print_1 = Printer("XEROX", "Phaser 3020", 8360)
print_2 = Printer("Canon", "G1411", 10900)
print_3 = Printer("Brother", "HL-1110R", 8990)
xerox_1 = Xerox("Canon", "2206iF", 129480)
xerox_2 = Xerox("Kyocera", "1801", 5159)
xerox_3 = Xerox("Canon", "FC108", 15380)

Scanner.to_ware(scan_1)
Scanner.to_ware(scan_2)
Scanner.to_ware(scan_3)
Printer.to_ware(print_1)
Printer.to_ware(print_2)
Printer.to_ware(print_3)
Xerox.to_ware(xerox_1)
Xerox.to_ware(xerox_2)
Xerox.to_ware(xerox_3)

while True:
    my_pro = input("Продолжить работу - 1, завершить работу - 0: ")
    if my_pro == "1":
        all_mov = input("Все товары на складе - 1\n"
                        "Узнать стоимость всех товаров на складе - 2\n"
                        "Выполнить операции со сканерами - 3\n"
                        "Выполнить операции с принтерами - 4\n"
                        "Выполнить операции с ксероксами - 5\n"
                        "Все товары в магазине - 6\n"
                        "Завершить работу - 0\n"
                        "Что бы вы хотели сделать (введите нужное число): ")
        if all_mov == "1":
            Warehouse.my_print()
            Warehouse.my_scan()
            Warehouse.my_xerox()
        elif all_mov == "2":
            Warehouse.all_count()
        elif all_mov == "3":
            Warehouse.my_scan()
            Warehouse.my_shop()
            scan_mov = input("Переместить товар со склада в магазин - 1\n"
                             # "Переместить товар из магазина на склад - 2\n"
                             "Завершить работу - 0\n"
                             "Что бы вы хотели сделать (введите нужное число): ")
            if scan_mov == "1":
                try:
                    scan_num = input("Для перемещения нужного товара в магазин введите его номер из списка: ")
                    Warehouse.to_shop1()
                    Warehouse.my_shop()
                except (IndexError, ValueError):
                    print("В списке нет такого номера.")
            elif scan_mov == "0":
                print("Работа завершена.")
                break
            else:
                print("Введите корректное значение.")
        elif all_mov == "4":
            Warehouse.my_print()
            Warehouse.my_shop()
            print_mov = input("Переместить товар со склада в магазин - 1\n"
                              # "Переместить товар из магазина на склад - 2\n"
                              "Завершить работу - 0\n"
                              "Что бы вы хотели сделать (введите нужное число): ")
            if print_mov == "1":
                try:
                    print_num = input("Для перемещения нужного товара в магазин введите его номер из списка: ")
                    Warehouse.to_shop2()
                    Warehouse.my_shop()
                except (IndexError, ValueError):
                    print("В списке нет такого номера.")
            elif print_mov == "0":
                print("Работа завершена.")
                break
            else:
                print("Введите корректное значение.")
        elif all_mov == "5":
            Warehouse.my_xerox()
            Warehouse.my_shop()
            xerox_mov = input("Переместить товар со склада в магазин - 1\n"
                              # "Переместить товар из магазина на склад - 2\n"
                              "Завершить работу - 0\n"
                              "Что бы вы хотели сделать (введите нужное число): ")
            if xerox_mov == "1":
                try:
                    xerox_num = input("Для перемещения нужного товара в магазин введите его номер из списка: ")
                    Warehouse.to_shop3()
                    Warehouse.my_shop()
                except (IndexError, ValueError):
                    print("В списке нет такого номера.")
            elif xerox_mov == "0":
                print("Работа завершена.")
                break
            else:
                print("Введите корректное значение.")
        elif all_mov == "6":
            Warehouse.my_shop()
        elif all_mov == "0":
            print("Работа завершена.")
            break
        else:
            print("Введите корректное значение.")
    elif my_pro == "0":
        print("Работа завершена.")
        break
    else:
        print("Введите корректное значение.")
