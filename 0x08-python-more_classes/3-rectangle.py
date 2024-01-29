#!/usr/bin/python3
"""
    Class definition for a Rectangle
"""


class Rectangle:
    """
        Initialize a new Rectangle with a specified width and height
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Retrieve value of width square
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            modify value of width square
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Retrieve value of height square
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            modify value of height square
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        my_recta = ""
        if self.__height == 0 or self.__width == 0:
            return my_recta
        for k in range(self.__height):
            for l in range(self.__width):
                my_recta += '#'
            if k < self.__height - 1:
                my_recta += '\n'
        return my_recta
