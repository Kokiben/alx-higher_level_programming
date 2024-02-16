#!/usr/bin/python3
"""Unit test for base
"""

import unittest
from models.rectangle import Rectangle


class TestRectan(unittest.TestCase):
    """definition unit test for rectangle model"""

    def test_initializat(self):
        rec1 = Rectangle(2, 5)
        self.assertEqual(rec1.id, Rectangle._Base__nb_objects)
        rec2 = Rectangle(1, 2)
        self.assertEqual(rec2.id, Rectangle._Base__nb_objects)


if __name__ == '__main__':
    unittest.main()
