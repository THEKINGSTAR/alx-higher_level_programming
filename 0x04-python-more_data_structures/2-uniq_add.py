#!/usr/bin/python3
def uniq_add(my_list=[]):
    u_list = []
    u_sum = 0
    for i in my_list:
        if i not in u_list:
            u_list.append(i)
    for s in u_list:
        u_sum = u_sum + s
    return (u_sum)
