#!/usr/bin/python3
def uppercase(str):
    nstr = ""
    upp = ""
    word = list(str)
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
    print("{}".format(""))
