#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY ONE FUNDCITON TO
returns the dictionary description with simple data structure
"""

import json


def class_to_json(obj):
    """
    Write a function that returns the dictionary description
    with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
    Prototype: def class_to_json(obj):
    obj is an instance of a Class
    All attributes of the obj Class are serializable:
        list, dictionary, string, integer and boolean
    """

    # if isinstance(my_obj, set):
    #   my_obj = list(my_obj)
    if isinstance(obj, (list, tuple)):
        dicn_des = [dicn_des(item) for item in obj]
        return (dic_des)
    elif isinstance(obj, dict):
        din_des = {din_des(ke): din_des(value) for key, value in obj.items()}
        return (din_des)
    elif isinstance(obj, (str, bool, int, float, type(None))):
        return (obj)
    else:
        return (str(obj))
