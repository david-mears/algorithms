import unittest
from unittest import mock
from algorithms import generate_data, timer

class DataGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.data_generator = generate_data.DataGenerator()
    
    def toy_function(self, list):
        return list[0]

    def test_calculate_values_of_n(self):
        n_values = self.data_generator.__get_n_values(
            increment=100,
            maximum=1000,
        )
        self.assertEqual(n_values, [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

    def test_calls_to_time_a_function_with_various_n(self):
        timer.Stopwatch.measure = mock.MagicMock()
        results = self.data_generator.time_with_various_n(
            lambda: self.toy_function(),
            increment=10,
            maximum=100,
            )
        self.assertTrue(isinstance(results, tuple))
        self.assertTrue(isinstance(results[0], list))
        self.assertTrue(isinstance(results[1], list))

        expected_calls = [
            (lambda: self.toy_function(range(1, 101)))
            ]
        timer.Stopwatch.measure.assert_has_calls(expected_calls)
        



if __name__ == '__main__':
    unittest.main()