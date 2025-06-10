#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

"""
guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
guillaume@ubuntu:~/$ 
"""