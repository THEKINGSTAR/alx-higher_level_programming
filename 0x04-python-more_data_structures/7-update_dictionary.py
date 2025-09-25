#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    k = key
    if k in a_dictionary:
        a_dictionary[k] = value
    else:
        a_dictionary[k] = value

    return a_dictionary
