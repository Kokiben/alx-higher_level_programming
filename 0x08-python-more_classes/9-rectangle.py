#!/usr/bin/python3
"""
    Class definition for a Rectangle
"""


class Rectangle:
    """
        Initialze rectangle a specified with width and
        height square
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        # self.print_symbol = '#'

    @property
    def width(self):
        """
            Retrieve value of width square
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Modify value of width square
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
            Modify value of height square
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Retrieve area width multiplied by height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Retrieve perimeter width plus height
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
            __str__
        """
        me_rect = ""
        if self.__height == 0 or self.__width == 0:
            return me_rect
        for a in range(self.__height):
            for k in range(self.__width):
                me_rect += str(self.print_symbol)
            if a < self.__height - 1:
                me_rect += '\n'
        return me_rect

    def __repr__(self):
        """
            __repr__
        """
        return "Rectangle(" + str(self.__width) + ', ' + str(self.__height)+')'

    def __del__(self):
        """
             __del__
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            method to return the bigger of 2 rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
