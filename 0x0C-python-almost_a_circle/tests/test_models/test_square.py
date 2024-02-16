#!/usr/bin/python3
""" unittest for square """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquarTestCas(unittest.TestCase):
    """ class definition for square test """

    def setUp(self):
        """
        Resets id
        """
        Base._Base__nb_objects = 0

    def test_squar_id_increment(self):
        pass


if __name__ == '__main__':
    unittest.main()
