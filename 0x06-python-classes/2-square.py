#!/usr/bin/python3
"""Class definition for a Square"""


class Square:
    """A simple represention of a square"""
    def __init__(self, size_leng=0):
        """
        Initialize a new Square with a specified side leng.

        Args:
            side_leng (int): The side leng of a square. Defaults to 0
        """
        if type(size_leng) is not int:
            raise TypeError("size_leng must be an integer")
        if size_leng < 0:
            raise ValueError("size leng must be >= 0")
        self.__size = size_leng
