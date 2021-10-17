class ComplexNumber:
    def __init__(self, str_complex_num):
        self.complex_number = self._check_input_data(str_complex_num)

    @classmethod
    def _check_input_data(cls, str_complex_num):
        try:
            complex_number = complex(str_complex_num)
            return complex_number
        except (AttributeError, ValueError) as error:
            print(f'ValueError: input "{str_complex_num}" cannot be'
                  f' converted to a complex number using the function'
                  f' "complex",  {error}.')

    def __str__(self):
        return f'{self.__class__.__name__}:' \
               f' {self.complex_number}, {type(self.complex_number)}.'

    def __truediv__(self, other):
        return ComplexNumber(self.complex_number / other.complex_number)

    def __mul__(self, other):
        return ComplexNumber(self.complex_number * other.complex_number)


a = ComplexNumber('1+1j')
b = ComplexNumber('2-1j')
print(a, b)
print(a * b)
c = ComplexNumber('112 rra')
