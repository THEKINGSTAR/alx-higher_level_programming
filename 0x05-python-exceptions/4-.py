#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    for idx in range(0, list_length):
        a = my_list_1[idx], b = my_list_2[idx]
        try:
            c = a / b
        except value:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        If my_list_1 or my_list_2 is too short
            print("out of range")
