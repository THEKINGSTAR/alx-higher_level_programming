#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def multi(inpt):
        return inpt * number
    new_list = list(map(multi, my_list))
    return new_list