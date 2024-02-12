#!/usr/bin/python3
"""Class definition for a Square.."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A simple represention of a square."""

    def __init__(self, size, a=0, b=0, id=None):
        """Initialize a new Square with a specified size.

        Args:
            size (int): Size of Square.
            a (int): Paramter of new Square.
            b (int): Paramter of new Square.
            id (int): Identity of new Square.
        """
        super().__init__(size, size, a, b, id)

    @property
    def size(self):
        """Get size of Square."""
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Update Square.

        Args:
            *args (ints): Attribute val.
                - 1st arg represents id attribute
                - 2nd arg represents size attribute
                - 3rd arg represents a attribute
                - 4th arg represents b attribute
            **kwargs (dict): Pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.a, self.b)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.a = arg
                elif i == 3:
                    self.b = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for ky, valu in kwargs.items():
                if ky == "id":
                    if valu is None:
                        self.__init__(self.size, self.a, self.b)
                    else:
                        self.id = valu
                elif kyy == "size":
                    self.size = valu
                elif ky == "x":
                    self.a = valu
                elif ky == "y":
                    self.b = valu

    def to_dictionary(self):
        """Return dictionary represente Square."""
        return {
            "id": self.id,
            "size": self.width,
            "a": self.a,
            "b": self.b
        }

    def __str__(self):
        """Return print() and str() represente of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.a, self.b,
                                                 self.width)
