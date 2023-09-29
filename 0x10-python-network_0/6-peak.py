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

"""
def find_peak(list_of_integers):
    # FIND PEAK FUNCTION
    ln = len(list_of_integers)
    lst = list_of_integers
    if (lst[ln / 2] < lst[ln / 2 - 1]):
        lst = [lst[0] : lst[ln / 2 - 1]]
    else if (lst[ln / 2] < lst[ln / 2 + 1]):
        lst = [lst[ln / 2]: lst[ln / 2 + 1]]
    else:
        return (lst[0])
"""


def find_peak(list_of_integers):
    """Find a peak element in a list of integers."""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return (list_of_integers[low])
