class Cell:
    one_part = '*'

    def __init__(self, parts):
        self.parts = int(parts)
        self._p_in_row = None

    def __str__(self):
        return f'This {self.__class__.__name__} consist of {self.parts} part(s).'

    def __add__(self, other):
        return Cell(self.parts + other.parts)

    def __sub__(self, other):
        if self.parts - other.parts > 0:
            return Cell(self.parts - other.parts)
        print(f'Number of parts less than 0.')

    def __mul__(self, other):
        return Cell(self.parts * other.parts)

    def __truediv__(self, other):
        if other.parts > 0:
            return Cell(round(self.parts / other.parts))
        print(f'It is impossible to divide by zero.')

    def make_order(self, p_in_row):
        self._p_in_row = int(p_in_row)
        result = []
        for i in range(self.parts):
            result.append(self.one_part)
            if (i + 1) % self._p_in_row == 0:
                result.append('\n')
        result = ''.join(result)
        return result


a = Cell(10)
b = Cell(4)
c = Cell(5)
print(a)
print(b)
print(a + b + c)
print(b - a)
print(a - b - c)
print(b * c)
print(b / c)
print(a.make_order(3))
