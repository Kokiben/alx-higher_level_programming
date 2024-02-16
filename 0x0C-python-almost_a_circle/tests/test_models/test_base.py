#!/usr/bin/python3
""" unittest for bases """
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class BasTestCass(unittest.TestCase):
    """ Class definition for a base test """
    def setUp(self):
        """
        Resets id
        """
        Base._Base__nb_objects = 0

    def test_bas_tak1(self):
        bas1 = Base()
        self.assertEqual(bas1.id, 1)

        bas2 = Base()
        bas3 = Base()
        self.assertEqual(bas2.id, 2)
        self.assertEqual(bas3.id, 3)

        bas4 = Base(12)
        bas5 = Base()
        self.assertEqual(bas4.id, 12)
        self.assertEqual(bas5.id, 4)


if __name__ == '__main__':
    unittest.main()
