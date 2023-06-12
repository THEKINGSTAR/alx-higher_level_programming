#!/usr/bin/python3

def multiple_returns(sentence):
    frst = sentence[0]
    lenght = len(sentence)
    if len(sentence) == 0:
        frst = None
    str_tup = (lenght, frst)
    return (str_tup)
