#!/usr/bin/python3
"""Create a function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """
    Function to create Pascal's Triangle with n rows..

    Args:
        n (int): Number of rows to generate in Pascal's Triangle..

    Returns:
        list: List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []
    trian = [[1]]
    for a in range(1, n):
        rw = [1]
        lst_rw = trian[-1]
        rw.extend([sum(pair) for pair in zip(lst_rw, lst_rw[1:])])
        rw.append(1)
        trian.append(rw)
    return trian
