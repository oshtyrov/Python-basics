user_input = 'oneoneoneone two three four five six seven eight nine ' \
             'tentententen'
user_list_input = user_input.split()
buff = 0
for el in user_list_input:
    if len(el) > 10:
        el = el[0:10]
    buff += 1
    print(f'{buff}: {el}.')

