# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
with open('docs/file_01.txt', 'w+', encoding='utf-8') as file:
    while True:
        user_input = input('Введите строку, для окончания работы программы'
                           'введите пустую строку: ')
        file.writelines(user_input + '\n')
        if not user_input:
            break
