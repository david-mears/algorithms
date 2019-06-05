import os
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt

class Plotter:
    
    # data as arrays
    # labels as strings
    def plot(self,
            x_data,
            y_data,
            x_label='N',
            y_label='time',
            ):
        plt.plot(x_data, y_data)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        file_name = ('%s.png' % str(datetime.now().timestamp()))
        file_path = os.path.join(os.getcwd(), 'plots', file_name)
        plt.savefig(file_path)
        return file_path