#!/usr/bin/python3
""" Function find_peak """

"""
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Write a function that finds a peak in a list of unsorted integers.

Prototype: def find_peak(list_of_integers):
You are not allowed to import any module
Your algorithm must have the lowest complexity
(hint: you don’t need to go through all numbers to find a peak)
6-peak.py must contain the function
6-peak.txt must contain the complexity of
your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
Note: there may be more than one peak in the list
"""


def find_peak(list_of_integers):
    """ FIND PEAK FUNCTION """
    if (len(list_of_integers) <= 0):
        return (None)
    m = 0
    c = 0
    s = len(list_of_integers)
    while (c < s - 1):
        p = list_of_integers[c]
        r = list_of_integers[c + 1]
        if (c != 0):
            f = list_of_integers[c - 1]
        else:
            f = None

        if (f is not None and r is not None and m < p):
            m = p
        c += 1
    return (m)
