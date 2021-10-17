class MyErrorZeroDiv(Exception):
    def __init__(self, text):
        self.txt = text


a = 100
b = 0


try:
    if b == 0:
        raise MyErrorZeroDiv(f'Сan not be divided by "{b}"!')
    c = a / b
except MyErrorZeroDiv as mr:
    print(mr)
else:
    print(c)

