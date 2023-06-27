#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(0, list_length):
        try:
            a = my_list_1[idx]
            b = my_list_2[idx]
            c = a / b
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            c = 0
            print("division by 0")
        except IndexError:
            print("out of range")
        new_list.append(c)
    return (new_list)
