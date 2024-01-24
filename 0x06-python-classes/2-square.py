#!/usr/bin/python3
"""Class definition for a Square"""


class Square:
    """A simple represention of a square"""
    def __init__(self, size=0):
        """
        Initialize a new Square with a specified size.

        Args:
            size (int): The size of a square. Defaults to 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
