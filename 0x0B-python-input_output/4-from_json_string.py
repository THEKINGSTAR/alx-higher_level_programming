#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY ONE FUNDCITON TO RETURN PYTHON OBJECT
"""


import json


def from_json_string(my_str):
    """
    Write a function that returns
    an object (Python data structure) represented by a JSON string:
    """
    python_obj = json.loads(my_str)
    return (python_obj)
