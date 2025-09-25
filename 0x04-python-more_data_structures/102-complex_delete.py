#!/usr/bin/python3
"""
15. Delete by value
"""


def complex_delete(a_dictionary, value):
    """
    function that deletes keys with a specific value in a dictionary.
    """

    list_of_keys: list = []

    for key in a_dictionary:
        if a_dictionary[key] == value:
            list_of_keys.append(key)

    for key in list_of_keys:
        del a_dictionary[key]
    return a_dictionary
