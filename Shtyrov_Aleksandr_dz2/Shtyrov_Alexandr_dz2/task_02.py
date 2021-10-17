my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
i = 0
while i < len(my_list):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2
    if len(my_list) - i == len(my_list) % 2:
        break
print(my_list)


