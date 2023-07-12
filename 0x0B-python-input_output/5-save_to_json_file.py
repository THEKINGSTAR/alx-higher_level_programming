#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY ONE FUNDCITON TO WRITE OBJECT INTO JSON FILE
"""

import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation:
    """

    # if isinstance(my_obj, set):
    #   my_obj = list(my_obj)

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False)
