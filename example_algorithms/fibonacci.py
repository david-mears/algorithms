class Fibonacci():

    def fibonacci(self, list):
        # convert list to n where the task is to return the first n fibonacci numbers
        n = len(list)
        sequence = []
        for i in range(1, n+1):
            if len(sequence) < 2:
                sequence.append(len(sequence))
            else:
                sequence.append(
                    sequence[-1] + sequence[-2]
                )
        return sequence