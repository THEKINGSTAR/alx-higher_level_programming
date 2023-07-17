#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle:

In the file models/square.py
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
Call the super class with id, x, y, width and height
- this super call will use the logic of the __init__ of the Rectangle class.
The width and height must be assigned to the value of size
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inheret and create square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """adding the public getter and setter size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """
        The setter should assign (in this order) the width and the height
        - with the same value
        The setter should have the same value validation as the Rectangle
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
         method that assigns attributes:
        """
        """
        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        **kwargs can be thought of as
        a double pointer to a dictionary: key/value (keyworded arguments)
        **kwargs must be skipped if *args exists and is not empty
        Each key in this dictionary represents an attribute to the instance
        """
        if len(args) >= 1:
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            return

        if kwargs.get("id"):
            self.id = kwargs["id"]
        if kwargs.get("size"):
            self.size = kwargs["size"]
        if kwargs.get("x"):
            self.x = kwargs["x"]
        if kwargs.get("y"):
            self.y = kwargs["y"]

    def to_dictionary(self):
        """
        adding the public method
        that returns the dictionary representation of a Square:
        This dictionary must contain:
        id
        size
        x
        y
        {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        """
        dict_rep = {}
        dict_rep["id"] = self.id
        dict_rep["x"] = self.x
        dict_rep["size"] = self.width
        dict_rep["y"] = self.y
        return (dict_rep)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
