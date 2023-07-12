#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY ONE FUNDCITON TO CEATE OBJECT FROM JSON
"""


import json


def load_from_json_file(filename):
    """
    Write a function that creates an
    Object from a “JSON file”:
    """
    with open(filename, 'r', encoding="utf-8") as file:
        data = file.read()
        python_obj = json.loads(data)
    return (python_obj)
