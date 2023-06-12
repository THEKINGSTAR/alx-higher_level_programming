#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return (my_list)
    # n_list = my_list[:idx] + my_list[idx + 1:]
    # my_list = n_list.copy()
    n_list = []
    del my_list[idx]
    n_list = my_list
    # print(my_list)
    # print(n_list)
    return (n_list)
