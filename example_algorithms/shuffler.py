from random import shuffle, randint

class Shuffle():

    def slow_shuffle(self, _list):
        list_length = len(_list)
        if list_length < 2:
            return _list
        new_list = []
        index = 0
        for i in list(range(list_length)):
            random_no = randint(0, len(_list) - 1)
            new_list.append(_list[random_no])
            _list.remove(_list[random_no])
            index += 1
        return new_list

    def better_shuffle(self, _list):
        list_length = len(_list)
        if list_length < 2:
            return _list
        new_list = []
        index = 0
        for i in list(range(list_length)):
            random_no = randint(0, len(_list) - 1)
            new_list.append(_list[random_no])
            _list[random_no] = _list.pop()
            index += 1
        return new_list

    def pythonshuffle(self, list):
        shuffle(list)