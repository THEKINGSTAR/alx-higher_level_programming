#!/usr/bin/env python3
'''
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
'''
import string

def uppercase(str):
    nstr = ""
    upp = ""
    for c in str[:]:
        if (ord(c) > 96) and (ord(c) < 123):
            ch = ord(c) - 32
            upp = chr(ch)
            nstr = nstr + upp
        elif (ord(c) > 48) and (ord(c) < 58):
           nstr = nstr + str(c) 
    print(nstr)
    return (nstr)
