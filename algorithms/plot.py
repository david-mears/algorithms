import os
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt

class Plotter:
    
    def plot(self, x_label, x_data, y_label, y_data):
        plt.plot([3, 4], [3, 4])
        plt.xlabel('number of eggs eaten')
        plt.ylabel('stars in the sky')
        file_name = ('%s.png' % str(datetime.now().timestamp()))
        file_path = os.path.join(os.getcwd(), 'plots', file_name)
        plt.savefig(file_path)
        return file_path