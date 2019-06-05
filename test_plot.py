import unittest
from algorithms import plot

class PlotTest(unittest.TestCase):

    # def setUp(self):
    #     self.plotter = plot.Plotter()

    def test_plotter_exists(self):
        self.plotter = plot.Plotter()

if __name__ == '__main__':
    unittest.main()
