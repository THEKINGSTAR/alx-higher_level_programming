#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matx = []
    new_matx = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    return new_matx
