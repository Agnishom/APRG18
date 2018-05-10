import importlib.util
import random
import math
import sys
import collections
import pickle

# load the test module
spec = importlib.util.spec_from_file_location("testModule", sys.argv[1])
testModule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(testModule)

#load the data
cases = pickle.load(open('cases.dat', 'rb'))

#Anagram Problem Solver
class AnagramProblemSolver:
    def __init__(self, wordList):
        self.anagramTable = {}
        for word in wordList:
            sortedWord = "".join(sorted(word))
            if sortedWord in self.anagramTable:
                self.anagramTable[sortedWord] += 1
            else:
                self.anagramTable[sortedWord] = 1

    def query(self, query):
        sortedQuery = "".join(sorted(query))
        if sortedQuery in self.anagramTable:
            return self.anagramTable[sortedQuery]
        else:
            return 0

#correctness for AnagramProblemSolver
testAnagramObj = testModule.AnagramProblemSolver(list(cases['wordList']))
anagramObj = AnagramProblemSolver(list(cases['wordList']))
correctCases = 0
for query in cases['queryList']:
    try:
        myAnswer = anagramObj.query(query)
        theirAnswer = testAnagramObj.query(query)
        assert(myAnswer == theirAnswer)
        correctCases += 1
    except:
        #print("Anagram Fails")
        #print(query)
        pass
print("AnagramProblemSolver:", correctCases, "cases passed")

# our solution to the BinarySearchTree
class BinarySearchTree:
    def __init__(self, initialList = None):
        self.table = {}
        if initialList != None:
            self.table = dict(initialList)

    def insert(self, key):
        if key in self.table:
            self.table[key] += 1
        else:
            self.table[key] = 1

    def count(self, key):
        if key in self.table:
            return self.table[key]
        else:
            return 0

# correctness for BinarySearchTree
correctCases = 0
testBSTobj = testModule.BinarySearchTree(cases['initialList'])
BSTobj = BinarySearchTree(cases['initialList'])
for (queryType, query) in cases['treeQueryList']:
    if queryType == "insert":
        testBSTobj.insert(query)
        BSTobj.insert(query)
    else:
        try:
            myAnswer = BSTobj.count(query)
            theirAnswer = testBSTobj.count(query)
            assert (myAnswer == theirAnswer)
            correctCases += 1
        except:
             #print("BinarySearchTree Fails")
             #print(query)
             pass
print("BinarySearchTree:", correctCases, "cases passed")
