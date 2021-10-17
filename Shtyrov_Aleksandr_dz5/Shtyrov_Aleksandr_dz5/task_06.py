def find_num(string):
    result = []
    i = 0
    while i < len(string):
        s_int = ''
        a = string[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < len(string):
                a = string[i]
            else:
                break
        i += 1
        if s_int != '':
            result.append(int(s_int))
    return result


with open('docs/file06.txt', 'r', encoding='utf-8') as file:
    file_data = file.read().splitlines()
    subjects_list = [file_data[i].split(':')[0] for i in range(len(file_data))]
    lessons_list = [sum(find_num(file_data[i])) for i in range(len(file_data))]
    sub_les_dict = dict(zip(subjects_list, lessons_list))
    print(sub_les_dict)
