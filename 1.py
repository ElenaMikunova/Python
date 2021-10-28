class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        self.new = ""
        for el in self.matrix:
            self.new += "   ".join(map(str, el)) + "\n\n"
        return f"{self.new}"

    def __add__(self, other):
        """ Можно убрать условие; в таком случае матрицы тоже будут перемножаться,
        но лишь те их значения, которые есть в каждой из начальных матриц."""
        if sum([len(el) for el in self.matrix]) == sum([len(el) for el in other.matrix]) \
                and len(self.matrix) == len(other.matrix):
            self.n = list(list(zip(el[0], el[1])) for el in list(zip(self.matrix, other.matrix)))
            self.all = []
            for el in self.n:
                self.count = []
                for x in el:
                    self.count.append(sum(x))
                self.all.append(self.count)
            return Matrix(self.all)
        else:
            return f"Невозможно сложить: матрицы разной длины\n\n"


matrix_1 = Matrix([[1, 2, 3], [3, 4, 5], [4, 3, 11]])
matrix_2 = Matrix([[5, 6, 74], [7, 8, 33], [3, 4, 12]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_2 + matrix_2 + matrix_1)

# matrix_3 = Matrix([[1, 2, 3], [3, 4, 5]])
# matrix_4 = Matrix([[5, 6, 74], [7, 8, 33], [3, 4, 12]])
# print(matrix_3)
# print(matrix_4)
# print(matrix_3 + matrix_4)
#
# matrix_5 = Matrix([[1, 2, 3], [3, 4]])
# matrix_6 = Matrix([[5, 6, 74], [7, 8, 33]])
# print(matrix_5)
# print(matrix_6)
# print(matrix_5 + matrix_6)
