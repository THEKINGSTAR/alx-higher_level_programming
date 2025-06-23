#!/usr/bin/python3
def no_c(my_string):
    strn = ""
    for ch in my_string:
        if ch == "c" or ch == "C":
            continue
        strn = strn + ch
    return (strn)
