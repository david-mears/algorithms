class SubSequenceSum():

    def breadth_first(self, list, target=0):
        # Each pass through the list expand the size of the summed sublist
        for i in range(1, len(list)):
            index = 0
            for j in list:
                sublist = list[index:index+i]
                if sum(sublist) == target:
                    return True
                index += 1
        return False

    # def depth_first(self, list, target=0):
    #     # Each pass, try all possible sublist sizes starting at one place in the list
    #     for i in range(1, len(list)):


        
