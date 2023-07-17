#!/usr/bin/python3
"""
Write the class Square that inherits from Rectangle:

In the file models/square.py
Class Square inherits from Rectangle
Class constructor: def __init__(self, size, x=0, y=0, id=None)::
Call the super class with id, x, y, width and height 
- this super call will use the logic of the __init__ of the Rectangle class. 
The width and height must be assigned to the value of size

You must not create new attributes for this class,
use all attributes of Rectangle - As reminder: a Square is a Rectangle with the same width and height

All width, height, x and y validation must inherit from Rectangle - same behavior in case of wrong data
The overloading __str__ method should return [Square] (<id>) <x>/<y> - <size> - in our case, width or height
As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle.
Now you have a Square class who has the same attributes and same methods.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class inheret and create square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y
        self.id = id

    @property
    def size(self):
        """adding the public getter and setter size"""
        return (self.width)
    @size.setter
    def size(self ,value):
        """
        The setter should assign (in this order) the width and the height - with the same value
        The setter should have the same value validation as the Rectangle
        for width and height - No need to change the exception error message (It should be the one from width)
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
        **kwargs can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
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
    
    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")