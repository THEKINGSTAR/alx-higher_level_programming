#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY ONE FUNDCITON TO WRITE DATA INTO FILE
"""


def write_file(filename="", text=""):
    """
    WRITE IN FILE FUNCTION
    """
    with open(filename, 'w', encoding="utf-8") as file:
        writen = file.write(text)
    return (writen)
