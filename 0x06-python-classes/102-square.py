#!/usr/bin/python3
"""Class definition for a Square."""


class Square:
    """Initialize a new Square with a specified size."""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int) or not isinstance(val, float):
            raise TypeError("size must be a number")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size
