#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        for k in range(len(matrix[a])):
            if k != 0:
                print(" ", end='')
            print("{:d}".format(matrix[a][k]), end="")
        print()
