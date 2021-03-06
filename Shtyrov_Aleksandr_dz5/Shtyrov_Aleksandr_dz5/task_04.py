# # 4. Создать (не программно) текстовый файл со следующим содержимым:
# # One — 1
# # Two — 2
# # Three — 3
# # Four — 4
# # Необходимо написать программу, открывающую файл на чтение и считывающую
# # построчно данные. При этом английские числительные должны заменяться на русские.
# # Новый блок строк должен записываться в новый текстовый файл.
s1 = {1: 'один',
      2: 'два',
      3: 'три',
      4: 'четыре',
      5: 'пять',
      6: 'шесть',
      7: 'семь',
      8: 'восемь',
      9: 'девять',
      0: ''}

s2 = {2: 'двадцать',
      3: 'тридцать',
      4: 'сорок',
      5: 'пятьдесят',
      6: 'шестьдесят',
      7: 'семьдесят',
      8: 'восемьдесят',
      9: 'девяносто'}

s3 = {1: 'сто',
      2: 'двести',
      3: 'триста',
      4: 'четыреста',
      5: 'пятьсот',
      6: 'шестьсот',
      7: 'семьсот',
      8: 'восемьсот',
      9: 'девятьсот'}

tsat = {10: 'десять',
        11: 'одиннадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать'}


def nir(s):
    p = []
    if len(s) > 1:
        if 9 < int(s[-2:]) < 20:
            p.append(tsat[int(s[-2:])])
        elif int(s[-2:]) > 19:
            p.append(s1[int(s[-1])])
            p.append(s2[int(s[-2])])
    else:
        if int(s[-1]) > 0:
            p.append(s1[int(s[-1])])
        else:
            p.append('ноль')
    if len(s) == 3:
        p.append(s3[int(s[-3])])
    return ' '.join(p[::-1])


with open('docs/file04.txt', 'r', encoding='utf-8') as file:
    file_data = list(map(str.strip, file.readlines()))
i = 0
while i < len(file_data):
    eng_num = file_data[i][:(file_data[i].find(' ')):]
    rus_num = nir(file_data[i][(file_data[i].rfind(' ')) + 1::])
    file_data[i] = file_data[i].replace(eng_num, rus_num.capitalize())
    i += 1
with open('docs/file04_2.txt', 'w', encoding='utf-8') as file_02:
    for line in file_data:
        file_02.write(line + '\n')
