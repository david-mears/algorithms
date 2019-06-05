import unittest
from algorithms import generate_data

class DataGeneratorTest(unittest.TestCase):

    def test_can_make_data_generator(self):
        self.data_generator = generate_data.DataGenerator()
        self.assertTrue(self.data_generator)

if __name__ == '__main__':
    unittest.main()