
import time

class Stopwatch():

    def measure(self, function):
        start_time = time.perf_counter()
        function()
        finish_time = time.perf_counter()
        return finish_time - start_time

