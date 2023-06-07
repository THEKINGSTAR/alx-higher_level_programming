#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number > 0:
        last_digit = (number % 10)
    elif number < 0:
        tmp = number * -1
        last_digit = (tmp % 10)
    return (last_digit)


"""
print(print_last_digit(98))
print(print_last_digit(0))
print(print_last_digit(-1024))
"""
