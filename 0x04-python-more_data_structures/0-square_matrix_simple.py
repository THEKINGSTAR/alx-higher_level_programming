#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matx = []
    sub = []

    for i in range(len(matrix)):
        sub = []
        for j in range(len(matrix[i])):
            sub.append(matrix[i][j] ** 2)
        n_matx.append(sub)

    return (n_matx)
