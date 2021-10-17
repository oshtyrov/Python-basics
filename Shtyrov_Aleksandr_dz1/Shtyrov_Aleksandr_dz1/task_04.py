# while True:
#     user_input = input('введите целое положительное число: ')
#     if user_input.isdigit():
#         user_input = int(user_input)
# user_input = "1234567890"
# while True:
#     user_numbers = []
#     for number in user_input:
#         user_numbers.append(int(number))
#     break

# maximum = 0
# for i in user_numbers:
#     if i > maximum:
#         maximum = i
# print(max)

user_input = "18234596780"
user_int_input = int("18234596780")
maximum = 0
i = 0
counter = 10
while i < len(user_input):
    variable = user_int_input % counter / counter
    i = i + 1
    counter = counter * 10
    if variable >= maximum:
        maximum = variable
print(int(maximum * 10))



















