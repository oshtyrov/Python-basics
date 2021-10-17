# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open('docs/file02.txt', 'r', encoding='utf-8') as file:
    lines_words_list = [line.split() for line in file]
    for i in range(len(lines_words_list)):
        words_in_str = (len(lines_words_list[i]))
        print(f'Длинна {i + 1}й строки - {words_in_str} слов.')
