#!/usr/bin/python3

"""Class definition for a base."""
import json
import csv
import turtle


class Base:
    """from models.base

    This serves as  the "base" for all other classes.

    Private Class Properties:
        __nb_object (int): count of created Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): this argument value a new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(dicti_lst):
        """Return the JSON format of a string entity.

        Args:
            dicti_lst (list): list of dictionaries.
        """
        if dicti_lst is None or dicti_lst == []:
            return "[]"
        return json.dumps(dicti_lst)

    @classmethod
    def save_to_json_file((fil, ob_lst):
        """Saves an Object to a text file, employing a JSON serialization.

        Args:
            ob_list (list): A list of inherited Base instances.
        """
        filename = fil.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dicti_lst = [s.to_dictionary() for s in ob_list]
                jsonfile.write(Base.to_json_string(dicti_lst))

    @staticmethod
    def from_json_string(mi_string):
        """Return an object represented by a JSON string..

        Args:
            mi_string (str): String representation of a list.
        Returns:
            If mi_string is None - an empty list.
            Otherwise - List represented by mi_string.
        """
        if mi_string is None or mi_string == "[]":
            return []
        return json.loads(mi_string)

    @classmethod
    def create(cs, **dictio):
        """Return class instantied from a dictionary.

        Args:
            **dictio (dict): Pairs of attributes to initial.
        """
        if dictio and dictio != {}:
            if cs.__name__ == "Rectangle":
                nw = cs(1, 1)
            else:
                nw = cs(1)
            nw.update(**dictio)
            return nw

    @classmethod
    def load_from_file(cs):
        """Return list of classes instante  from fil of JSON str.

        Reads from `<cls.__name__>.json`.

        Returns:
            If fil does not exist - an empty list.
            Otherwise - List of instante classes.
        """
        filnam = str(cs.__name__) + ".json"
        try:
            with open(filnam, "r") as jsonfile:
                lst_dicts = Base.from_json_string(jsonfile.read())
                return [cs.create(**d) for d in lst_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cs, lst_obj):
        """Create a CSV serialization of list of objects to fil.

        Args:
            list_objs (list): List of inherited Base.
        """
        filnam = cs.__name__ + ".csv"
        with open(filnam, "w", newline="") as csvfile:
            if lst_obj is None or lst_obj == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for ob in lst_obj:
                    writer.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cs):
        """Return list of classes instante a CSV fil.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If file does not exist - an empty list.
            Otherwise - list of instante classes.
        """
        filnam = cs.__name__ + ".csv"
        try:
            with open(filnam, "r", newline="") as csvfile:
                if cs.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                lst_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                lst_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in lst_dicts]
                return [cs.create(**d) for d in lst_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(lst_recta, lst_squa):
        """Draw Rectangles and Squares use turtle.

        Args:
            lst_recta (list): List Rectangle objects.
            lst_squa (list): List Square objects.
        """
        trt = turtle.Turtle()
        trt.screen.bgcolor("#b7312c")
        trt.pensize(3)
        trt.shape("turtle")

        trt.color("#ffffff")
        for rect in lst_recta:
            trt.showturtle()
            trt.up()
            trt.goto(rect.x, rect.y)
            trt.down()
            for a in range(2):
                trt.forward(rect.width)
                trt.left(90)
                trt.forward(rect.height)
                trt.left(90)
            trt.hideturtle()

        trt.color("#b5e3d8")
        for sq in lst_squa:
            trt.showturtle()
            trt.up()
            trt.goto(sq.x, sq.y)
            trt.down()
            for a in range(2):
                trt.forward(sq.width)
                trt.left(90)
                trt.forward(sq.height)
                trt.left(90)
            trt.hideturtle()

        trtle.exitonclick()
