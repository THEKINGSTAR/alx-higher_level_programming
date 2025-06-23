#!/usr/bin/python3
def is_index_empty(tup, index):
    if index >= 0 and index < len(tup):
        return not bool(tup[index])

def add_tuple(tuple_a=(), tuple_b=()):
    if is_index_empty(tuple_a, 0):
        a1 = 0
    elif is_index_empty(tuple_b, 0):
        b1 = 0
    elif is_index_empty(tuple_a, 1):
        a2 = 0
    elif is_index_empty(tuple_b, 1):
        b2 = 0
    else:
        a1 = tuple_a[0]
        b1 = tuple_b[0]
        a2 = tuple_a[1]
        b2 = tuple_b[1]
        
    a = a1 + b1
    b = a2 + b2
    tuple_sum = (a,b)
    return (tuple_sum)
