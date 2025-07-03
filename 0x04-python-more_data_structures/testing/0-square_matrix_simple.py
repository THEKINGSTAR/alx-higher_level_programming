#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
        computes the square value of all integers of a matrix
    '''
    def mtx_sqr(a):
        return a**2


    # return_matx = [[mtx_sqr(num) for num in row] for row in matrix]
    return_matx = list(map(lambda row: list(map(mtx_sqr, row)), matrix))

    return list(return_matx)

if __name__ == "__main__":
    matrix = [
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19]
    ]
    print (square_matrix_simple(matrix))
