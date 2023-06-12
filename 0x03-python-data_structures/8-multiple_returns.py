#!/usr/bin/python3

def multiple_returns(sentence):
    frst = sentence[0]
    lenght = 0
    print(sentence)
    if len(sentence) == 0:
        frst = None
        lenght = 0
    else:
        lenght = len(sentence)
    str_tup = (lenght, frst)
    return (str_tup)
