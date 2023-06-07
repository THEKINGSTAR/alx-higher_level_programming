#!/usr/bin/python3
for o in range(0, 10):
    for t in range(1, 10):
        if (o != 8 and t != 9):
            if o != t and o < t:
                print("{}{}, ".format(o, t), end="")
        elif o == 8 and t == 9:
            print("{}{}".format(o, t))
