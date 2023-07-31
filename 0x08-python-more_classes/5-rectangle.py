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
    def width(self):
        """to retrieve it"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """to set it:
            width must be an integer, otherwise"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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

    def area(self):
        """Public instance method: that returns the rectangle area"""
        area = (self.height * self.width)
        return (area)

    def perimeter(self):
        """Public instance method: that returns the rectangle perimeter:"""
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = (self.height * 2) + (self.width * 2)
        return (perimeter)

    def __str__(self):
        """should print the rectangle with the character #:
        if width or height is equal to 0, return an empty string
        """
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            str_rep = ""
            for h in range(self.height):
                for w in range(self.width):
                    str_rep += "#"
                if h != (self.height - 1):
                    str_rep += "\n"
            return (str_rep)

    def __repr__(self):
        """
        should return a string representation of the rectangle
        to be able to recreate a new instance
        by using eval() (see example below)
        You are not allowed to import any module
        """
        str_reps = (f"Rectangle({self.width}, {self.height})")
        return (str_reps)

    def __del__(self):
        """
        Print the message 'Bye rectangle...'
        (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted
        """
        del (self)

        print("Bye rectangle...")
