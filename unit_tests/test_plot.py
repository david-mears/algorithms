import unittest
import os
from algorithms import plot

class PlotTest(unittest.TestCase):

    def setUp(self):
        self.plotter = plot.Plotter()

    def test_plotter_creates_files(self):
        file_location = self.plotter.plot(
            x_label='n', x_data=[0, 1, 2], y_label='time', y_data=[0, 1, 2]
            )
        self.assertTrue(os.path.exists(file_location))
