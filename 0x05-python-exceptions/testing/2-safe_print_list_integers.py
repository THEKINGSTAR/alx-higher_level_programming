#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for n in range(0, x):
        try:
            print("{:d}".format(my_list[n]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
