def countIslands(mapString):
    """
    count the number of islands in the given map
    :param mapString: This is a string representing a matrix of 0's and 1's, which represents a discrete map of land and water
    :returns: an int, the number of islands
    """
    ...
    return ...

def countBridges(vertexCount, adjacencyLists):
    """
    count the number of bridges in the given graph, with vertices labelled from 1 to vertexCount (inclusive)
    :param vertexCount: The number of vertices in the graph
    :param adjacencyLists: A dictionary of vertexCount lists of integers (from 1 to vertexCount). adjacencyLists[u] is a list consisting of the neighbors of the uth vertex
    :returns: an int, the number of bridges in the graph
    """
    ...
    return ...

def sequenceJump(markings):
	"""
	find the minimum number of moves to reach the last stone starting from first stone
	:param markings: List of marking sequence of the stones
	:returns: an int, minimum number of moves required
	"""
	...
	return ...

def main():
    map1 = "111000\n100010\n001001\n010101\n100000\n000111"
    map2 = "111\n111\n111"
    print(countIslands(map1) == 4) # should print True
    print(countIslands(map2) == 1) # should print True
    graph1 = {1: [2, 3], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5, 6], 5: [4, 6], 6: [4, 5]}
    print(countBridges(6, graph1) == 1) # should print True

    print(sequenceJump([2018, 1986, 2002, 1847, 2018]) == 1) # should print True
    print(sequenceJump([0,1,2,1,3,4,4,4,4,4,4,4,4,4,3]) == 4) # should print True

if __name__ == "__main__":
    main()
