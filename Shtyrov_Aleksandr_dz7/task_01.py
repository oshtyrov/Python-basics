a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

b = [
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18]
]

c = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.sum_result = None

    def __str__(self):
        return f'{self.__class__.__name__}: {self.matrix}.'

    def _calc_sum(self, other):
        self.sum_result = []
        for el, elem in zip(self.matrix, other.matrix):
            sum_el = [el[i] + elem[i] for i, _ in enumerate(self.matrix)]
            self.sum_result.append(sum_el)
        return self.sum_result

    def __add__(self, other):
        self.sum_result = self._calc_sum(other)
        return Matrix(self.sum_result)


mat1 = Matrix(a)
mat2 = Matrix(b)
mat3 = Matrix(c)
print(mat1)
print(mat2)
print(mat3)
d = mat1 + mat2
e = mat1 + mat2 + mat3
print(d)
print(e)
