#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for c in r:
            if c != r[-1]:
                print("{:d} ".format(c), end="")
            else:
                print("{:d}".format(c), end="")
        print("")
