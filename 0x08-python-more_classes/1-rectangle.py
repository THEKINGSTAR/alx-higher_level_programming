#!/usr/bin/python3
"""
module containe only one class
"""


class Rectangle:
    """
    define Rectangle class
    """
    def __init__(self, width=0, height=0):
        """ initit vlues """
        self.height = height
        self.width = width

    @property
    def height(self):
        """to retrieve it"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """to set it:height must be an integer, otherwise"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """to retrieve it"""
        return (slef.__width)

    @width.setter
    def width(self, value):
        """to set it:
            width must be an integer, otherwise"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
