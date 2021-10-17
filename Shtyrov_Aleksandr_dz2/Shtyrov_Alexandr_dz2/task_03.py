user_input = '10'
my_dict_month = {'1': 'zima', '2': 'zima','3': 'vesna', '4': 'vesna',
                  '5': 'vesna', '6': 'leto', '7': 'leto', '8': 'leto',
                  '9': 'osen', '10': 'osen', '11': 'osen', '12': 'zima'}
my_list_mounth = [1, 'zima', 2, 'zima', 3, 'vesna', 4, 'vesna', 5, 'vesna', 6, 'leto',
                  7, 'leto', 8, 'leto', 9, 'osen', 10, 'osen', 11, 'osen', 12, 'zima']
for key in my_dict_month:
    if key == user_input:
        print(my_dict_month[key])

user_input = int(user_input)
for val in my_list_mounth:
    if val == user_input:
        time_index = my_list_mounth.index(val)
        print(my_list_mounth[time_index + 1])






