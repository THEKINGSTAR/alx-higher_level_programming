#!/usr/bin/python3

"""
this module containe one function lookup
that list all the atribute of calss
"""


def lookup(obj):
    """
    class obj to look for its atributes
    """
    at_lst = []
    for ob in dir(obj):
        at_lst.append(ob)
    return (at_lst)
