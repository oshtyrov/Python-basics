import json

with open('docs/file07.txt', 'r', encoding='utf-8') as file:
    file_data = [line.split() for line in file]
all_firm_dict = {}
average_profit_dict = {}
firm_in_profit = 0
sum_firm_in_profit = 0
for i in range(len(file_data)):
    file_data[i][2], file_data[i][3] = \
        int(file_data[i][2]), int(file_data[i][3].replace('.', ''))
    file_data[i][2] -= file_data[i][3]
    all_firm_dict[file_data[i][0]] = file_data[i][2]
    if file_data[i][2] > 0:
        firm_in_profit += 1
        sum_firm_in_profit += file_data[i][2]
average_profit_dict['average_profit'] = round((sum_firm_in_profit / firm_in_profit), 2)
result_list = [all_firm_dict, average_profit_dict]
print(result_list)
with open('docs/file07.json', 'w') as j_file:
    json.dump(result_list, j_file)
