import random

class Node:
    # this will be the nodes for the linked list
    def __init__(self, key, value=1):
        # this is the constructor for the Node which requires a key and a value
        # fill in the ellipsis below with appropriate code
        self.key = ...
        self.value = ...
        self.left = None
        self.right = None
    def setLeft(self, leftChild):
        # update the left child
        assert (leftChild == None or type(leftChild) == type(self)) # the given argument is either a null reference, or actually a node
        assert (leftChild.key < self.key) # check that while adding a left child, the BST property is maintained
        # fill in the rest below
        ...
    def setRight(self, rightChild):
        # update the right child
        assert (rightChild == None or type(rightChild) == type(self)) # the given argument is either a null reference, or actually a node
        assert (rightChild.key > self.key) # check that while adding a left child, the BST property is maintained
        # fill in the rest below
        ...
    def increment(self):
        # increment the value of the node by 1
        ...

class BinarySearchTree:
    # the class for the BinarySearchTree
    def __init__(self, initialList = None):
        # initialList is a list of (key, val) pairs
        if initialList == None:
            # if initialList is None, set self.isEmpty to True
            self.isEmpty = True
        else:
            # first shuffle the list
            # (Think: Why is doing this a good idea?)
            random.shuffle(initialList)
            # insert each element in the list one by one
            ...
    def isEmpty(self):
        # tells if the SearchTree is Empty
        return self.isEmpty
    def count(self, key):
        # if the given key is not present return 0
        # if it is present return the associated value
        ...
        return ...
    def insert(self, key):
        # if the given key is present, add one to its value
        # if it is not present, add it to the search tree and with value 1
        ...

class AnagramProblemSolver:
    # this class does not represent any meaningful data structure as such
    # but stands for the problem solving class for the anagram problem
    def __init__(self, wordList):
        # preprocess the wordList
        ...
    def query(self, query):
        # how many anagrams of the given query string exist?
        ...
        return ...


def main():
    # we'd have some test cases for the BinarySearchTree here
    someBigWordList = ["aba", "aab", "bbb"] # this could potentially be a list much larger
    anagramObj = AnagramProblemSolver(someBigWordList)
    listOfqueries = ["baa", "aaa"] # this could also potentially be much larger
    for query in listOfqueries:
        print(anagramObj.query(query))
        # the first given query above would print 2, since there are two anagrams of "baa" in the wordList
        # the other query should print 0, since there are no anagrams of "aaa" in the wordList

if __name__ == "__main__":
    main()
