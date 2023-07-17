#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONE CLASS
Call the super class with id
- this super call with use the logic of the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor:
        Call the super class with id
        - this super call with use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Private instance attributes,
        each with its own public getter and setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer.")
        if value <= 0:
            raise ValueError("width must be > 0.")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Private instance attributes,
        each with its own public getter and setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("height must be > 0.")
        self.__height = value

    @property
    def x(self):
        """
        Private instance attributes,
        each with its own public getter and setter
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Private instance attributes,
        each with its own public getter and setter
        """
        if type(value) != int:
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0.")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Private instance attributes,
        each with its own public getter and setter
        """
        if type(value) != int:
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value

    def area(self):
        """
        public method
        def area(self):
        that returns the area value of the Rectangle instance.
        """
        return (self.height * self.width)

    def display(self):
        """
        public method
        def display(self):
        that prints in stdout the Rectangle instance
        with the character # - you don’t need to handle x and y here
        """
        if self.height == 0 or self.width == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    # def update(self, *args):
        """
        adding the public method def update(self, *args):
        that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        This type of argument is called a no-keyword argument
        - Argument order is super important.
        """
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        """
    def update(self, *args, **kwargs):
        """
        **kwargs can be thought of as
        a double pointer to a dictionary: key/value
        that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        if kwargs.get("id"):
            self.id = kwargs["id"]
        if kwargs.get("width"):
            self.width = kwargs["width"]
        if kwargs.get("height"):
            self.height = kwargs["height"]
        if kwargs.get("x"):
            self.x = kwargs["x"]
        if kwargs.get("y"):
            self.y = kwargs["y"]

    def to_dictionary(self):
        """
        adding the public method
        that returns the dictionary representation of a Rectangle:
        This dictionary must contain:
        id
        width
        height
        x
        y
        {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        """
        dict_rep = {}
        dict_rep["x"] = self.x
        dict_rep["y"] = self.y
        dict_rep["id"] = self.id
        dict_rep["height"] = self.height
        dict_rep["width"] = self.width

        return (dict_rep)

    def __str__(self):
        """
        overriding the
        __str__ method so that it
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (f"[Rectangle] ({self.id}) \
                {self.x}/{self.y} - {self.width}/{self.height}")
