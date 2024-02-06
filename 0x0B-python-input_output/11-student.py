!/usr/bin/python3
"""Class Definition for  Student."""


class Student:
    """A simple represention of a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): Name first of student.
            last_name (str): Name last of student.
            age (int): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Provide the dictionary depiction of the Student."""
        return self.__dict__

    def reload_from_json(self, json):
        """Exchange all characteristics of the Student.

        Args:
            json (dict): A dictionar containing key-value pairs to substitute student characteristics.
        """
        for g, d in json.items():
            setattr(self, g, d)
