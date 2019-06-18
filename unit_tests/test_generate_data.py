import unittest
from unittest import mock
from algorithms import generate_data, timer

class DataGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.data_generator = generate_data.DataGenerator()
    
    def toy_function(self, list):
        return list[0]

    def test_calculate_values_of_n(self):
        n_values = self.data_generator.get_n_values(
            increment=100,
            maximum=400,
        )
        self.assertEqual(n_values, [100, 200, 300, 400])

    def test_returns_correct_type(self):
        results = self.data_generator.time_with_various_n(
            lambda list: self.toy_function(list),
            increment=10,
            maximum=100,
            )
        self.assertTrue(isinstance(results, tuple))
        self.assertTrue(isinstance(results[0], list))
        self.assertTrue(isinstance(results[0][0], int))
        self.assertTrue(isinstance(results[1], list))