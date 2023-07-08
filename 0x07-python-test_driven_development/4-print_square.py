#!/usr/bin/python3
"""
Module contains one function:
that print square
Usage:
print_square(size)

For exampler
>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    print square represented by character #
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
        return
    if size < 0:
        raise ValueError('size must be >= 0')
        return
    for s in range(0, size):
        for q in range(0, size):
            print("#", end="")
        print()
