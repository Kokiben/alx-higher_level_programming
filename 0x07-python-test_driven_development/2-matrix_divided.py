#!/usr/bin/python3
"""
This is "2-matrix_divided".

that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides elements in matrix"""
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    siz = None
    for a in matrix:
        if type(a) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if siz is None:
            siz = len(a)
        elif siz != len(a):
            raise TypeError("Each row of the matrix must have the same size")
        for k in a:
            if type(k) is not int and type(k) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(k / div, 2) for k in a] for a in matrix]
