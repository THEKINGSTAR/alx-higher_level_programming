#!/usr/bin/python3
""" Check """
from models.square import Square

s = Square(5, 1, 4, 3)
s.update(89, 6, 2)

if s.id != 89:
    print("ID of the Square must be updated to 89: {}".format(s.id))
    exit(1)

if s.size != 6:
    print("Size of the Square must be updated to 6: {}".format(s.size))
    exit(1)

if s.x != 2:
    print("X of the Square must be updated to 2: {}".format(s.x))
    exit(1)
    
print("OK", end="")
