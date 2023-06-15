#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matx = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            n_matx.append(matrix[i][j] ** 2)

    return (n_matx)
