# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,а
# при достижении числа 10 завершаем цикл. Во втором также необходимо
# предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle
from sys import argv

# user_args = argv
user_args = ('название файла', '3')


def first_iter(*args):
    if len(args) == 2:
        for element in count(int(args[1])):
            if element > 10:
                break
            else:
                print(element)
    else:
        print('Неверное количество аргуметов')


first_iter(*user_args)


# some_list = argv
some_list = ['1', '2', '3', '4', '5', '6', 'seven', 'eight', 'nine', 'ten']


def second_iter(*args):
    flag = 0
    for element in cycle(args):
        print(element)
        flag += 1
        if flag >= len(args):
            break


second_iter(*some_list)
