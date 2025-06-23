#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lst = my_list.copy()
    for i in my_list:
        if i % 2 == 0:
            new_lst[i] = True
        else:
            new_lst[i] = False
    return(new_lst)
