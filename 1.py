class Data:
    def __init__(self, number=input("Введите дату: ")):
        self.number = number

    @classmethod
    def numbering(cls):
        try:
            num_list = list(map(int, Data().number.split("-")))
            return num_list
        except ValueError:
            return "Данные введены некорректно."

    @staticmethod
    def validation():
        try:
            list(map(int, Data().number.split("-")))
            if (31 >= Data().numbering()[0] >= 1) \
                    and (12 >= Data().numbering()[1] >= 1) \
                    and (2021 > Data().numbering()[2] >= 0) \
                    and len(Data().numbering()) == 3:
                return "Спасибо, отличная дата!"
            else:
                return "Дата не похожа на настоящую."
        except ValueError:
            return "Данные всё ещё введены некорректно."


data_1 = Data()
print(data_1.numbering())
print(data_1.validation())
