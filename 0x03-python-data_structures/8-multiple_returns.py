#!/usr/bin/python3

def multiple_returns(sentence):
    frst = " "
    lenght = 0
    if len(sentence) == 0:
        frst = None
    elif len(sentence) > 0:
        frst = sentence[0]
        lenght = len(sentence)

    str_tup = (lenght, frst)
    return (str_tup)
