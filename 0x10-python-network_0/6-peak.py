#!/usr/bin/python3
"""Print a function for finds a peak."""


def find_peak(list_of_integers):
    """return peak."""
    if list_of_integers == []:
        return None

    siz = len(list_of_integers)
    if siz == 1:
        return list_of_integers[0]
    elif siz == 2:
        return max(list_of_integers)

    M = int(siz / 2)
    pk = list_of_integers[M]
    if pk > list_of_integers[M - 1] and pk > list_of_integers[M + 1]:
        return pk
    elif pk < list_of_integers[M - 1]:
        return peak_f(list_of_integers[:M])
    else:
        return peak_f(list_of_integers[M + 1:])
