def my_func(first, second, third):
    if second >= first <= third:
        return second + third
    elif first >= second <= third:
        return first + third
    else:
        return first + second


print(my_func(5, 4, 9))

