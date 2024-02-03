#!/usr/bin/python3
"""Unittest for max_integer(list=[])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer"""
    def testmod_docstring(self):
        """test module docsting"""
        n = __import__('6-max_integer').__doc__
        self.assertTrue(len(n) > 1)

    def testfunc_docstring(self):
        """Test funstion docstring"""
        k = max_integer.__doc__
        self.assertTrue(len(k) > 1)

    def testemp_list(self):
        """Test for list []"""
        i = []
        self.assertIsNone(max_integer(i))

    def testn_args(self):
        """Test no args to function pass"""
        self.assertIsNone(max_integer())

    def testone_elem(self):
        """Test only one number in list"""
        m = [1]
        self.assertEqual(max_integer(m), 1)

    def testposi_end(self):
        """Test all positive with max at end"""
        i = [4, 10, 8, 38, 16, 60]
        self.assertEqual(max_integer(i), 60)

    def testposi_middle(self):
        """Test all positive with max in middle"""
        n = [4, 10, 8, 380, 16, 60]
        self.assertEqual(max_integer(n), 380)

    def testposi_begin(self):
        """Test all positive with max at beginning"""
        c = [300, 10, 8, 38, 16, 40]
        self.assertEqual(max_integer(c), 300)

    def testone_nega(self):
        """Test list with one negative number"""
        nc = [300, 10, 8, -38, 16, 60]
        self.assertEqual(max_integer(nc), 300)

    def testall_nega(self):
        """Test for list with all negative numbers"""
        j = [-8, -60, -75, -1, -200]
        self.assertEqual(max_integer(j), -1)

    def testnone(self):
        """Test for passing none as arg"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def testnint_arg(self):
        """Test a non-integer type in list"""
        sti = [1, 2, "kaout", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(sti)

if __name__ == "__main__":
    unittest.main()
