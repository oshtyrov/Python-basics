# while True:
#     number = input('введите число от 0 до 9: ')
number = '5'
if number.isdigit() and 0 <= int(number) <= 9:
    number = int(number)
    result = (number + number * 11 + number * 111)
    print(result)
        # break

