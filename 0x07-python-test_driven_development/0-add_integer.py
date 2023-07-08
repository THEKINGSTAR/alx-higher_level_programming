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
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
        return
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
        return
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    sum = int(a + b)
    return (sum)
