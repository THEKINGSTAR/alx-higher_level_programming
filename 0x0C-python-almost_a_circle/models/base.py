#!/usr/bin/python3

"""
Create a file named models/base.py:

Class Base:

private class attribute __nb_objects = 0

class constructor: def __init__(self, id=None)::

if id is not None,
assign the public instance attribute id with this argument value
- you can assume id is an integer and you dont need to test the type of it
otherwise,
increment __nb_objects
and
assign the new value to the public instance attribute id

This class will be the base� of all other classes in this project.

The goal of it is to manage id attribute in all your future classes
and
to avoid duplicating the same code (by extension, same bugs)
"""
import turtle
import sys
import json


class Base:
    """
    The Base model.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor:
        set the id to 1 if none
        or increase it by 1
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON is one of the standard formats for sharing data representation.
        adding the that returns the
        JSON string representation of list_dictionaries:
        list_dictionaries is a list of dictionaries
        If list_dictionaries is None or empty, return the string: "[]"
        Otherwise,
        return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Update the class Base by adding the static method
        that returns the list of the JSON string representation json_string:
        json_string is a string representing a list of dictionaries
        If json_string is None or empty, return an empty list
        Otherwise, return the list represented by json_string
        """
        if json_string is None or len(json_string) < 1:
            return ([])
        dictionary = json.loads(json_string)
        return (dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:,
        using a JSON representation:
        list_objs is a list of instances who inherits of Base
        - example: list of Rectangle or list of Square instances
        You must use the static method to_json_string (created before)
        You must overwrite the file if it already exists
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_of_ditcns = [ob.to_dictionary() for ob in list_objs]
                get_json = cls.to_json_string(list_of_ditcns)
                file.write(get_json)

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        # Set the screen size
        screen.setup(width=800, height=600)

        # Create a turtle object for drawing
        t = turtle.Turtle()

        # Set the turtle speed and shape
        t.speed(1)
        t.shape("turtle")

        # Draw the rectangles
        for rectangle in list_rectangles:
            Base.draw_shape(t, rectangle)

        # Draw the squares
        for square in list_squares:
            Base.draw_shape(t, square)

        turtle.done()

    @staticmethod
    def draw_shape(t, shape):
        # Set the starting position
        t.penup()
        t.goto(shape.x, shape.y)
        t.pendown()

        # Draw the shape
        t.fillcolor("red")
        t.begin_fill()
        for _ in range(2):
            t.forward(shape.width)
            t.right(90)
            t.forward(shape.height)
            t.right(90)
        t.end_fill()

        # Reset the turtle's position
        t.penup()
        t.home()


"""
# Example usage
# Define some rectangles and squares
rect1 = Rectangle(100, 50, 50, 50)
rect2 = Rectangle(200, 100, 0, 0)
square1 = Square(150, 100, 100)
square2 = Square(75, -50, -50)

# Call the draw function with the rectangles and squares
draw([rect1, rect2], [square1, square2])
"""
