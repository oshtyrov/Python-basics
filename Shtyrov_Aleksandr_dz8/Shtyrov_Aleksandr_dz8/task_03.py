class MyError(Exception):
    def __init__(self, text, data):
        self.txt = text
        self.data = data


result_list = []

while True:
    try:
        user_input = input(
            'Введите число, для завершения работы программы введите "stop": ')
        if user_input == 'stop':
            print(result_list)
            break
        if not user_input.isdigit():
            raise MyError('Введенное значение не является числом', user_input)
        result_list.append(user_input)
    except MyError as mr:
        print(f'MyError: {mr}')
