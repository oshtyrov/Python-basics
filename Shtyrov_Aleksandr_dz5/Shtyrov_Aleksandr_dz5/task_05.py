# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('docs/file05.txt', 'w', encoding='utf-8') as file:
    file.write('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15')

with open('docs/file05.txt', 'r', encoding='utf-8') as file:
    file_data = file.read().split(' ')
    file_data_int = [int(num) for num in file_data]
    print(f'Сумма чисел в строке равна: {sum(file_data_int)}')
