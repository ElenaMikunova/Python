class Cell:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f"Количество ячеек в клетке - {self.x}."

    def __add__(self, other):
        return Cell(self.x + other.x)

    def __sub__(self, other):
        if self.x - other.x < 0:
            return "Невозможно выполнить вычитание."
        else:
            return Cell(self.x - other.x)

    def __mul__(self, other):
        return Cell(self.x * other.x)

    def __truediv__(self, other):
        if self.x // other.x == 0:
            return "Клетка исчезла."
        else:
            return Cell(self.x // other.x)

    def make_order(self, raw):
        order = ((("*" * raw) + "\n") * (self.x // raw)) + ("*" * (self.x % raw)) + "\n"
        return order


cell_1 = Cell(19)
cell_2 = Cell(8)
cell_3 = Cell(11)
print(cell_1 + cell_2 + cell_3)
print(cell_2 - cell_3)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2 / cell_3)
print(cell_1.make_order(4))
print(cell_2.make_order(3))
