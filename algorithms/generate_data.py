from algorithms import timer

class DataGenerator():
    INCREMENT = 500
    MAXIMUM = 10000

    def time_with_various_n(
        self,
        function,
        increment=INCREMENT,
        maximum=MAXIMUM,
        ):
        pass

    def __get_n_values(self, increment, maximum):
        n_values = []
        while increment <= maximum:
            n_values.append(maximum)
            maximum -= increment
        n_values.reverse()
        return n_values