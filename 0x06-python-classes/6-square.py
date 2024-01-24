#!/usr/bin/python3

"""Class definition for a Square"""


class Square:
    """Initialize a new Square with a specified size."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, val):
        if (not isinstance(val, tuple) or
                len(val) != 2 or
                not all(isinstance(nu, int) for nu in val) or
                not all(nu >= 0 for nu in val)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = val

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        [print() for a in range(self.__position[1])]
        for a in range(self.__size):
            [print(" ", end="") for l in range(self.__position[0])]
            [print("#", end="") for m in range(self.__size)]
            print()
