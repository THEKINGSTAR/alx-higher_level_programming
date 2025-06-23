#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    a1 = a[0] if len(a) > 0 and a[0] is not None else 0
    a2 = a[1] if len(a) > 1 and a[1] is not None else 0
    b1 = b[0] if len(b) > 0 and b[0] is not None else 0
    b2 = b[1] if len(b) > 1 and b[1] is not None else 0
    return (a1 + b1, a2 + b2)
