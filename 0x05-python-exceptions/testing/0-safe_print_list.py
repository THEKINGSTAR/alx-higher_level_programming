#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    """
    elm = 0
    for n in range(0, x):
        try:
            print(my_list[n], end="")
            elm += 1
        except IndexError:
                break            
    print("")
    return elm
