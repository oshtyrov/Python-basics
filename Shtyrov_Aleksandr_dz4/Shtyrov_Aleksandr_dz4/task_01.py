# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт
# с параметрами.
from sys import argv

my_args = argv


def payroll_preparation(*args):
    if len(args) == 4:
        return int(args[1]) * int(args[2]) + int(args[3])
    elif len(args) == 3:
        return int(args[1]) * int(args[2])
    else:
        print('Неверное количетсво аргументов.')


# print(payroll_preparation(*my_args))
print(payroll_preparation('название файла', '2', '2', '4'))
print(payroll_preparation('название файла', '2', '2'))
print(payroll_preparation('название файла', '2'))


