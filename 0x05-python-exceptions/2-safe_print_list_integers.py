#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
            except Exception:
                continue
    except IndexError:
        print(IndexError)
    print("")
    return (count)
