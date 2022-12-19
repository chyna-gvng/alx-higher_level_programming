#!/usr/bin/python3
# function that does exactly the same,
# sh*t as the python bytecode *provided*


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except:
            result = a + b
            break
    return result
