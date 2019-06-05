import unittest
import time
from algorithms import timer

class NewTest(unittest.TestCase):

    def setUp(self):
        self.stopwatch = timer.Stopwatch()

    def test_stopwatch_runs_functions(self):
        def raise_error():
            raise ValueError('desired error')
        
        with self.assertRaises(ValueError) as cm:
            self.stopwatch.measure(lambda:
                raise_error()
            )

        self.assertEqual(str(cm.exception), 'desired error')

    def test_stopwatch_times_functions(self):
        # Pass lambda function to the stopwatch
        duration = self.stopwatch.measure(lambda:
            time.sleep(1)
        )
        # Should return a length of time i.e. a float
        self.assertTrue(isinstance(duration, float))

        self.assertTrue(duration > 1)
        self.assertTrue(duration < 2)
    
if __name__ == '__main__':
    unittest.main()
