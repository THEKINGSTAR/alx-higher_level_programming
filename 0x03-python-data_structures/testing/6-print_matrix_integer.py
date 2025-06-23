#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for r in i:
            if r != i[-1]:
                print("{}".format(r), end=" ")
            else:
                print("{}".format(r), end="")
        print("")
