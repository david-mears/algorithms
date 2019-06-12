from algorithms import timer
from random import shuffle

class DataGenerator():
    INCREMENT = 500
    MAXIMUM = 10000

    def time_with_various_n(
        self,
        function,
        increment=INCREMENT,
        maximum=MAXIMUM,
        ):

        n_values = self.get_n_values(increment, maximum)
        datasets = []
        for n in n_values:
            _list = list(range(1, n+1))
            shuffle(_list)
            datasets.append(_list)
        
        times = []

        # Run the function once to get past the initial anomalies
        function(datasets[0])

        for dataset in datasets:
            time = timer.Stopwatch().measure(
                lambda: function(dataset)
            )
            times.append(time)
        results = (n_values, times)
        return results

    def get_n_values(self, increment, maximum):
        n_values = []
        while increment <= maximum:
            n_values.append(maximum)
            maximum -= increment
        n_values.reverse()
        return n_values