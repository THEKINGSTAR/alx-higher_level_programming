#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY ONE FUNDCITON TO RETURN JSON
"""


import json


def to_json_string(my_obj):
    """
    Write a function that returns
    the JSON representation of an object (string):
    """
    return (json.dumps(my_obj))
