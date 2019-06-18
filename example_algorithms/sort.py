from random import shuffle

class Sort():

    def bubble_sort(self, list):
        n = len(list)
        for i in range(n):
            for j in range(0, n-i-1):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]

    def bogosort(self, list):
        def is_sorted():
            index = 0
            for i in range(len(list) - 1):
                if list[i] > list[index+1]:
                    return False
                index += 1
            return True
        while not is_sorted():
            shuffle(list)

    def pythonsort(self, list):
        list.sort()