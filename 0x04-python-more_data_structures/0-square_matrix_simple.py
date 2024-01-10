#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for row in matrix:
        n_row = [elemnt ** 2 for elemnt in row]
        n_matrix.append(n_row)

    return n_matrix
