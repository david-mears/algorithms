from algorithms import timer

class DataGenerator():
    
    def get_n_values(self, increment=500, maximum=10000):
        n_values = []
        while increment <= maximum:
            n_values.append(maximum)
            maximum -= increment
        n_values.reverse()
        return n_values