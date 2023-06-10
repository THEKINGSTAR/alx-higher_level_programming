#!/usr/bin/python3
'''
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
'''


def uppercase(stri):
    nstr = ""
    upp = ""
    word = list(stri)
    # print(word)
    for c in word:
        if (ord(c) > 96) and (ord(c) < 123):
            ch = ord(c) - 32
            upp = chr(ch)
            nstr = nstr + upp
        elif (ord(c) > 48) and (ord(c) < 58):
            nstr = nstr + str.format(c)
        else:
            nstr = nstr + c
    print("{}".format(nstr), end="")
    print("")

