#!/usr/bin/python3
"""Unittest for max_integer(list=[])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""
    def test_module_docstring(self):
        """test module docsting"""
        n = __import__('6-max_integer').__doc__
        self.assertTrue(len(n) > 1)

    def test_function_docstring(self):
        """Test funstion docstring"""
        k = max_integer.__doc__
        self.assertTrue(len(k) > 1)

    def test_empty_list(self):
        """Test for list []"""
        i = []
        self.assertIsNone(max_integer(i))

    def test_no_args(self):
        """Test no args to function pass"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Test only one number in list"""
        m = [1]
        self.assertEqual(max_integer(m), 1)

    def test_positive_end(self):
        """Test all positive with max at end"""
        i = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(i), 50)

    def test_positive_middle(self):
        """Test all positive with max in middle"""
        n = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(n), 360)

    def test_positive_beginning(self):
        """Test all positive with max at beginning"""
        c = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(c), 200)

    def test_one_negative(self):
        """Test list with one negative number"""
        nc = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(nc), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        j = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(j), -1)

    def test_none(self):
        """Test for passing none as arg"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Test  a non-integer type in list"""
        sti = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(sti)

if __name__ == "__main__":
    unittest.main()
