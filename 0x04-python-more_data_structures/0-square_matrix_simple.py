#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matx = matrix.copy()
    for i in range(len(n_matx)):
        for j in range(len(n_matx[i])):
            n_matx[i][j] = n_matx[i][j] **2   
            
    return (n_matx)
