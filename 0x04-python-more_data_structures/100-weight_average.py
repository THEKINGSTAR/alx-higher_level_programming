#!/usr/bin/python3
def weight_average(my_list=[]):
    avg, sumtn, demon = 0, 0, 0
    if my_list is None or len(my_list) <= 0:
        return None
    for itm in my_list:
        sumtn += (itm[1] * itm[0])
        demon += itm[1]
    avg = sumtn / demon
    return avg
