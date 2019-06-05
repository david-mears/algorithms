import unittest
from algorithms import generate_data

class DataGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.data_generator = generate_data.DataGenerator()

    def test_can_calculate_values_of_n(self):
        n_values = self.data_generator.get_n_values(
            increment=100,
            maximum=1000,
        )
        self.assertEqual(n_values, [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

    

if __name__ == '__main__':
    unittest.main()