#!/usr/bin/python3
"""Class definition for  a Rectangle."""
from models.base import Base


class Rectangle(Base):
    """A simple represention of a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle with a specified width and height.

        Args:
            width (int): Width of new rectangle.
            height (int): Height of new rectangle.
            x (int): Paramter of  new rectangle.
            y (int): Paramter of new rectangle.
            id (int): Identity of new rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set width of rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """Set height of rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def a(self):
        """Set a paramter of rectangle."""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """Set y paramter of rectangle."""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using the `#` char."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for l in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update rectangle.

        Args:
            *args (ints): Attribute val.
                - 1st arg represents id attribute
                - 2nd arg represents width attribute
                - 3rd arg represent height attribute
                - 4th arg represents x attribute
                - 5th arg represents y attribute
            **kwargs (dict): Pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for ky, valu in kwargs.items():
                if ky == "id":
                    if valu is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = valu
                elif ky == "width":
                    self.width = valu
                elif ky == "height":
                    self.height = valu
                elif ky == "x":
                    self.x = valu
                elif ky == "y":
                    self.y = valu

    def to_dictionary(self):
        """Return dictionary represente a rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() represente rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
