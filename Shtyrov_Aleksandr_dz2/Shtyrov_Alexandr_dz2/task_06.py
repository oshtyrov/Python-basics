# number_of_goods = int(input('Введите количество товаров в вашей базе данных: '))
number_of_goods = int('1')
my_list_result = []
my_analytical_dict = {}
name_analytical_list = []
prise_analytical_list = []
how_many_analytical_list = []
unit_analytical_list = []
i = 1
while i <= number_of_goods:
    # name = input(f'Введите название {i}-го товара: ')
    name = 'панталоны'
    name_analytical_list.append(name)
    # prise = input(f'Введите цену {i}-го товара: ')
    prise = int('100')
    prise_analytical_list.append(prise)
    # how_many = input(f'Введите количество едениц {i}-го товара: ')
    how_many = int('5')
    how_many_analytical_list.append(how_many)
    # unit = input(f'Введите еденици измерения {i}-го товара: ')
    unit = 'унция'
    if unit_analytical_list.count(unit) == 0:
        unit_analytical_list.append(unit)
    my_default_str = f"{{'название': '{name}', 'цена': {prise}, 'количество': {how_many}, 'eд': '{unit}'}}"
    my_default_dict = eval(my_default_str)
    my_default_lft = []
    my_default_lft.append(i)
    my_default_lft.append(my_default_dict)
    my_default_tuple = tuple(my_default_lft)
    my_list_result.append(my_default_tuple)
    i += 1
my_analytical_dict['название'] = name_analytical_list
my_analytical_dict['цена'] = prise_analytical_list
my_analytical_dict['количество'] = how_many_analytical_list
my_analytical_dict['ед'] = unit_analytical_list
print(my_list_result)
print(my_analytical_dict)








