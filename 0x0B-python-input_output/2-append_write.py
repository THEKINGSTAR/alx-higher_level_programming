#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY ONE FUNDCITON TO APPEND DATA INTO FILE
"""


def append_write(filename="", text=""):
    """
    WRITE IN FILE FUNCTION
    """
    with open(filename, 'a', encoding="utf-8") as file:
        writen = file.write(text)
    return (writen)
