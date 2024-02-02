#!/usr/bin/python3
"""
Define function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div.

    Args:
    matrix : List of lists of integers/floats.
    div : The Factor.
    Raises:
    TypeError: If matrix includes non-numbers.
    TypeError: If matrix includes rows of different sizes.
    TypeError: If divide is not an integer or float.
    ZeroDivisionError: If divide is 0.

    Returns:
    A new matrix.
    """
    if matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for node in row:
            if not (isinstance(node, int) or isinstance(node, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats")
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_div = []
    for row in matrix:
        row_mat = []
        for node in row:
            sut = round(node / div, 2)
            row_mat.append(sut)
        matrix_div.append(row_mat)
    return matrix_div
