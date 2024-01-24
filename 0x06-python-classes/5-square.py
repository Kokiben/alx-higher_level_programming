#!/usr/bin/python3

"""Class definition for a Square"""


class Square:
    """Initialize a new Square with a specified size."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for a in range(self.__size):
            for b in range(self.__size):
                print("#", end="")
            print()
