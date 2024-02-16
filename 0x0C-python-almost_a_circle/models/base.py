#!/usr/bin/python3

"""Class definition for a base."""
import json
import csv
import turtle


class Base:
    """Base model.

    This Represents "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
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
        """Return JSON serialization of list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of list of objects to file.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return deserialization of JSON str.

        Args:
            json_string (str): JSON string representation of a list of dictionary.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return class instantied from dictionary of attributes.

        Args:
            **dictionary (dict): Pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                nw = cls(1, 1)
            else:
                nw = cls(1)
            nw.update(**dictionary)
            return nw

    @classmethod
    def load_from_file(cls):
        """Return list of classes instantiated from file of JSON str.

        Reads from `<cls.__name__>.json`.

        Returns:
            If file does not exist - an empty list.
            Otherwise - List of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV serialization of list/objects to file.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for ob in list_objs:
                    writer.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return list of classes instantiated from CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If file does not exist - an empty list.
            Otherwise - List of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([ky, int(va)] for ky, va in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles/squares using turtle module.

        Args:
            list_rectangles (list): List of rectangle objects to draw.
            list_squares (list): List of square objects to draw.
        """
        trt = turtle.Turtle()
        trt.screen.bgcolor("#b7312c")
        trt.pensize(3)
        trt.shape("turtle")

        trt.color("#ffffff")
        for re in list_rectangles:
            trt.showturtle()
            trt.up()
            trt.goto(re.x, re.y)
            trt.down()
            for k in range(2):
                trt.forward(re.width)
                trt.left(90)
                trt.forward(re.height)
                trt.left(90)
            trt.hideturtle()

        trt.color("#b5e3d8")
        for squ in list_squares:
            trt.showturtle()
            trt.up()
            trt.goto(squ.x, squ.y)
            trt.down()
            for k in range(2):
                trt.forward(squ.width)
                trt.left(90)
                trt.forward(squ.height)
                trt.left(90)
            trt.hideturtle()

        turtle.exitonclick()
