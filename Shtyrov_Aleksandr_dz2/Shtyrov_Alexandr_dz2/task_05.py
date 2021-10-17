my_list = [7, 5, 3, 3, 2]
user_input = int('1')
if my_list.count(user_input) > 0:
    my_list.insert(my_list.index(user_input), user_input)
else:
    for number in my_list:
        if number < user_input:
            my_list.insert(my_list.index(number), user_input)
            break
        elif my_list[-1] > user_input:
            my_list.append(user_input)
            break
print(my_list)
