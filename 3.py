class Worker:

    def __init__(self, a, b, c, d, e):
        self.name = a
        self.surname = b
        self.position = c.capitalize()
        self._income = {"wage": d, "bonus": e}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.position}: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход сотрудника {self.name} {self.surname}: {sum(self._income.values())} рублей.")


manager = Position("Иван", "Иванов", "менеджер", 20000, 3400)
manager.get_full_name()
manager.get_total_income()
counter = Position("Петр", "Петров", "бухалтер", 30000, 5000)
counter.get_full_name()
counter.get_total_income()
