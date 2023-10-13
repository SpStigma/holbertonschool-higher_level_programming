# project/tests/max_integer_test.py

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    A test suite for the max_integer function.
    """
    
    def test_max_integer_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Expected None for an empty list")

    def test_max_integer_positive_numbers(self):
        result = max_integer([1, 3, 5, 2, 4])
        self.assertEqual(result, 5, "Expected 5 for the list [1, 3, 5, 2, 4]")

    def test_max_integer_negative_numbers(self):
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1, "Expected -1 for the list [-1, -3, -5, -2, -4]")

    def test_max_integer_mixed_numbers(self):
        result = max_integer([1, -3, 5, -2, 4])
        self.assertEqual(result, 5, "Expected 5 for the list [1, -3, 5, -2, 4]")

    def test_max_integer_duplicate_max(self):
        result = max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3, "Expected 3 for the list [3, 3, 3, 3]")

    def test_max_integer_single_element(self):
        result = max_integer([7])
        self.assertEqual(result, 7, "Expected 7 for the list [7]")

    def test_max_integer_empty_list_default_arg(self):
        result = max_integer()
        self.assertIsNone(result, "Expected None for an empty list (default argument)")

if __name__ == '__main__':
    unittest.main()