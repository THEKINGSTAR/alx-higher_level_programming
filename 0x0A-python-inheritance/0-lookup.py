#!/usr/bin/python3

def lookup(obj):
    at_lst = []
    for ob in dir(obj):
        at_lst.append(ob)
    return (at_lst)
