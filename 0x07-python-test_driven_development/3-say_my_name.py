#!/usr/bin/python3

"""
This is the "print" module.supplies one function,
say_my_name("f_name", "l_name").
For example,
>>> say_my_name("John", "Smith")
My name is John Smith$
"""


def say_my_name(first_name, last_name=""):
    """
    print first or last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
