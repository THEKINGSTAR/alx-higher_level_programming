#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(0, list_length):
        try:
            a = my_list_1[idx]
            b = my_list_2[idx]
            c = a / b
        except IndexError:
            print("out of range")
            c = 0
        except TypeError:
            print("wrong type")
            c = 0
        except ZeroDivisionError:
            c = 0
            print("division by 0")
        finally:
            new_list.append(c)
    return (new_list)
