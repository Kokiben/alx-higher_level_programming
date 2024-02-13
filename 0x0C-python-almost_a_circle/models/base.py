#!/usr/bin/python3

"""Class definition for a base."""
import json
import csv
import turtle


class Base:
    """Base model.

    This represents "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instante Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): Identity of new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON serialization of list of dicts.

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Print JSON serialization of list of objects to file.

        Args:
            list_objs (list): List of inherited Base instance.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [j.to_dictionary() for j in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return deserialization of a JSON sti.

        Args:
            json_string (str): JSON string represente list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - Python list represente by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return class instantied dictionary for attributes.

        Args:
            **dictionary (dict): Pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                w = cls(1, 1)
            else:
                w = cls(1)
            w.update(**dictionary)
            return w

    @classmethod
    def load_from_file(cls):
        """Return list of classes instante a file of JSON str.

        Reads from `<cls.__name__>.json`.

        Returns:
            If file does not exist - an empty list.
            Otherwise - List of instantiated classes.
        """
        filnam = str(cls.__name__) + ".json"
        try:
            with open(filnam, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**c) for c in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Print CSV serialization of list of objects to fil.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        filnam = cls.__name__ + ".csv"
        with open(filnam, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fdnames = ["id", "width", "height", "x", "y"]
                else:
                    fdnames = ["id", "size", "x", "y"]
                wrter = csv.DictWrter(csvfile, fdnames=fdnames)
                for ob in list_objs:
                    wrter.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return list of classes instante CSV fil.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If file does not exist - an empty list.
            Otherwise - List of instantiated classes.
        """
        filnam = cls.__name__ + ".csv"
        try:
            with open(filnam, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fdnames = ["id", "width", "height", "a", "b"]
                else:
                    fdnames = ["id", "size", "a", "b"]
                list_dicts = csv.DictReader(csvfile, fdnames=fdnames)
                list_dicts = [dict([ky, int(valu)] for ky, valu in c.items())
                              for c in list_dicts]
                return [cls.create(**c) for c in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and Squares using turtle.

        Args:
            list_rectangles (list): List of rectangle objects to draw.
            list_squares (list): List of Square objects to draw.
        """
        trt = turtle.Turtle()
        trt.screen.bgcolor("#b7312c")
        trt.pensize(3)
        trt.shape("turtle")

        trt.color("#ffffff")
        for rectan in list_rectangles:
            trt.showturtle()
            trt.up()
            trt.goto(rectan.x, rectan.y)
            trt.down()
            for m in range(2):
                trt.forward(rectan.width)
                trt.left(90)
                trt.forward(rectan.height)
                trt.left(90)
            trt.hideturtle()

        trt.color("#b5e3d8")
        for squa in list_squares:
            trt.showturtle()
            trt.up()
            trt.goto(squa.x, squa.y)
            trt.down()
            for m in range(2):
                trt.forward(squa.width)
                trt.left(90)
                trt.forward(squa.height)
                trt.left(90)
            trt.hideturtle()

        turtle.exitonclick()
