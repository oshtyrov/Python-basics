def sum_user_input():
    result = 0
    q_signal = False
    while q_signal is False:
        # user_input = input('Введите строку чисел, разделенных пробелом,'
        #                    'для завершения работы программы введите "q":')
        user_input = '1 2 3 4 q 5'
        ui_list = user_input.split()
        for number in ui_list:
            if number == 'q':
                q_signal = True
                break
            result += int(number)
        print(result)


sum_user_input()
