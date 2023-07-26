#!/usr/bin/python3
"""
this module contain MyList that inherits from list:
"""


class MyList(list):
    """
    Public instance method:
    that prints the list,
    but sorted (ascending sort)
    """
    def print_sorted(self):
        print(sorted(self))
