# def my_func(x, y):
#     return x ** y


def my_func_2(x, y):
    i = 0
    positive_result = x
    while i < abs(y) - 1:
        positive_result *= x
        i += 1
    return 1 / positive_result


print(my_func_2(5, -2))
