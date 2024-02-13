#!/usr/bin/python3
"""Class definition for a Square.."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A simple represention of a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square with a specified size.

        Args:
            size (int): Size of new Square.
            x (int):  Paramter of new Square.
            y (int):   Paramter of the new Square.
            id (int): Identity of new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size of Square."""
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Update square.

        Args:
            *args (ints): Attribute values.
                - 1st arg represents id attribute
                - 2nd arg represents size attribute
                - 3rd arg represents x attribute
                - 4th arg represents y attribute
            **kwargs (dict): Pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for ky, valu in kwargs.items():
                if ky == "id":
                    if valu is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = valu
                elif ky == "size":
                    self.size = valu
                elif ky == "x":
                    self.x = valu
                elif ky == "y":
                    self.y = valu

    def to_dictionary(self):
        """Return dictionary represente of Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return print() and str() represente square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
