#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n_list = []
    for tf in my_list:
        if tf % 2 == 0:
            n_list.append(True)
        else:
            n_list.append(False)
    return (n_list)
