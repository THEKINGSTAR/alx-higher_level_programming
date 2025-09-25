#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("Size Type Must Be Integer")
        if size < 0:
            raise ValueError("Size Must Be > 0.")
        self.__size = size
    def area(self):
        return (self.__size ** 2)
