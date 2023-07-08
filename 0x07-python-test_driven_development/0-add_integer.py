#!/usr/bin/python3
"""
This is the "add" module.supplies one function, add_integer().  For example,
>>> add_integer(5, 6)
11
"""


def add_integer(a, b=98):
    """
    Returns an integer: the addition of a and b
    """
    sum = 0
    if type(a) is not int:
        raise TypeError("a must be an integer or b must be an integer")
        return
    if type(b) is not int:
        raise TypeError("a must be an integer or b must be an integer")
        return
    sum = int(a + b)
    return (sum)
