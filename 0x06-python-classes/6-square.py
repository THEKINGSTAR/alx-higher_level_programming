#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 4-square.py)

Private instance attribute: size:

property def size(self): to retrieve it

property setter def size(self, value): to set it:

size must be an integer,
otherwise raise a TypeError exception with the message size must be an integer

if size is less than 0,
raise a ValueError exception with the message size must be >= 0

Instantiation with optional size: def __init__(self, size=0):

Public instance method:
def area(self): that returns the current square area

Private instance attribute: position:
property def position(self): to retrieve it

property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers,
otherwise raise a TypeError exception with the
message: position must be a tuple of 2 positive integers

Instantiation with optional size and optional position:
def __init__(self, size=0, position=(0, 0)):

Public instance method: def area(self):
that returns the current square area

Public instance method: def my_print(self):
that prints in stdout the square with the character #:

if size is equal to 0, print an empty line

position should be use by using space
-Don’t fill lines by spaces when position[1] > 0

You are not allowed to import any module
"""


class Square:
    """Write a class Square that defines a square by: (based on 1-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
            len(value) != 2 or \
                not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """
    Public instance method: def area(self):
        that returns the current square area
    You are not allowed to import any module
    """
    def area(self):
        return (self.__size ** 2)
    """
    Public instance method:
    def my_print(self): that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line

    position should be use by using space -
    Don’t fill lines by spaces when position[1] > 0
    """
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for s in range(self.__position[1]):
                print()
            for x in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
