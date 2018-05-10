def largestSumSubsequence(sequence):
    """
    return the sum of the largest contiguous subsequence in the given sequence

    :param sequence: list of ints
    :returns: an int
    """
    ...
    return ...

def freeTime(start, end, intervals):
    """
    return the number of time units the machine is free for (including the starting and ending point, potentially)

    :param start: int, the time from when the machine is available
    :param end: int, the time till when the machine is available
    :param intervals: list of (two tuples of ints)
    :returns: an int
    """
    ...
    return ...

class MedianKeeper:
    def __init__(self):
        # initialize as you want to
        ...
    def update(self, val):
        """
        add the value val to the current dataset (assume that you never have to deal with duplicates)

        :param val: int
        """
        ...
    def query(self):
        """
        return the current median

        :returns: a float
        """
        ...
        return ...

def canTravel(L, adjacencyLists):
    """
    check if Deeparaj can travel from Chennai (0) to Bangalore (1)

    :param L: int, the number of units Deeparaj can go without having to stop to refuel
    :param adjacencyLists:
    """
    ...
    return ...

def main():
    list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(largestSumSubsequence(list1) == 7) #should print True
    intervals1 = [(1, 2), (2, 3), (5, 7), (6, 7), (10, 10)]
    print(freeTime(0, 10, intervals1) == 4) # should print True
    medianKeeperInstance = MedianKeeper()
    medianKeeperInstance.update(1)
    print(medianKeeperInstance.query() == 1) # should print True (since the current set is {1})
    medianKeeperInstance.update(5)
    medianKeeperInstance.update(3)
    print(medianKeeperInstance.query() == 3) # should print True (since the current set is {1, 3, 5})
    graph1 = {0: [(1, 2)], 1: [(1, 3)], 2: [(1, 0), (2, 3)], 3:[(2, 2), (1, 1)]}
    graph2 = {0: [(1, 2)], 1: [(1, 3)], 2: [(1, 0), (1, 3)], 3:[(1, 2), (1, 1)]}
    print(not canTravel(1, graph1)) # should print True
    print(canTravel(1, graph2)) # should print True

if __name__ == "__main__":
    main()
