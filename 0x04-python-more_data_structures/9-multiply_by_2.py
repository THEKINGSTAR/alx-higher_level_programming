#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for k in a_dictionary:
        new_dict[k] = a_dictionary[k] * 2
    return new_dict
