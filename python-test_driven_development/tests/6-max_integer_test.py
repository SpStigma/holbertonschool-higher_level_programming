# project/tests/max_integer_test.py

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

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

    def test_max_integer_all_negative_numbers(self):
        result = max_integer([-1, -3, -5, -2, -4])
        self.assertEqual(result, -1, "Expected -1 for the list [-1, -3, -5, -2, -4]")

    def test_max_integer_mixed_numbers_with_zeros(self):
        result = max_integer([1, 0, -3, 5, -2, 4])
        self.assertEqual(result, 5, "Expected 5 for the list [1, 0, -3, 5, -2, 4]")

    def test_max_integer_float_numbers(self):
        result = max_integer([1.5, 3.7, 2.2, 4.9])
        self.assertEqual(result, 4.9, "Expected 4.9 for the list [1.5, 3.7, 2.2, 4.9]")

    def test_max_integer_large_numbers(self):
        result = max_integer([10**18, 10**19, 10**20])
        self.assertEqual(result, 10**20, "Expected 10^20 for the list [10^18, 10^19, 10^20]")

    def test_max_integer_string_elements(self):
        result = max_integer(['a', 'b', 'c'])
        self.assertIsNone(result, "Expected None for the list ['a', 'b', 'c']")

    def test_max_integer_list_with_none_values(self):
        result = max_integer([1, None, 3, None, 5])
        self.assertEqual(result, 5, "Expected 5 for the list [1, None, 3, None, 5]")

    def test_max_integer_list_with_nan_inf(self):
        result = max_integer([float('nan'), float('inf')])
        self.assertTrue(result != result, "Expected NaN as result")

if __name__ == '__main__':
    unittest.main()