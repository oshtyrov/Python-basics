# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
with open('docs/file03.txt', 'r', encoding='utf-8') as file:
    file_data = [line.split() for line in file]
    less_then_20 = [person[0] for person in file_data if int(person[1]) < 20]
    medium_pay = [int(person[1]) for person in file_data]
    print(f'Фамилии сотрудников, чей оклад меньше 20 тыс.:'
          f' {", ".join(less_then_20)}.')
    print(f'Средняя зароботная плата равна: '
          f'{sum(medium_pay) / len(medium_pay)} тыс.')
