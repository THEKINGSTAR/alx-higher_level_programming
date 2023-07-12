#!/usr/bin/python3
"""
THIS MODULE CONTAIN ONLY ONE FUNDCITON TO READ INPUT FILE
"""


def read_file(filename=""):
    """
    READ FILE FUNCTION
    """
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
    print(read_data, end="")
