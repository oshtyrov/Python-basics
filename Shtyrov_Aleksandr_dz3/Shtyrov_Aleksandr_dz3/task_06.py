def int_func(ui_str):
    ui_list = ui_str.split()
    i = 0
    while i < len(ui_list):
        ui_list[i] = ui_list[i].capitalize()
        i += 1
    print(*ui_list)


int_func('Aaa bbb ccc')
