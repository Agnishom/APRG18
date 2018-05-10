import importlib.util
import random
import math
import sys
import collections
import pickle
import plotTree
from PIL import Image
import pygame, sys, os
from pygame.locals import *

# load the test module
spec = importlib.util.spec_from_file_location("testModule", sys.argv[1])
testModule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(testModule)

# load the source module
spec = importlib.util.spec_from_file_location("sourceModule", sys.argv[2])
sourceModule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sourceModule)

#load the data
cases = pickle.load(open('cases.dat', 'rb'))
queryLists = cases['queryLists']


# the isomorphism checker
def isIsomorphic(Node1, Node2):
    if Node1 == None and Node2 == None:
        return True
    if Node1.nodeType != Node2.nodeType:
        return False
    nodeType = Node1.nodeType
    if nodeType == 2:
        if Node1.d1 != Node2.d1:
            return False
        return isIsomorphic(Node1.c1, Node2.c1) and isIsomorphic(Node1.c2, Node2.c2)
    elif nodeType == 3:
        if not (Node1.d1, Node1.d2 == Node2.d1, Node2.d2 or Node1.d2, Node1.d1 == Node2.d1, Node2.d2):
            return False
        return isIsomorphic(Node1.c1, Node2.c1) and isIsomorphic(Node1.c2, Node2.c2) and isIsomorphic(Node1.c3, Node2.c3)

# a visualization subroutine
def visualize():
    pygame.init()
    screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)
    testTreeObj = testModule.TwoThreeTree()
    #for (queryType, query) in queryList:
    for (queryType, query) in [("insert", i) for i in range(100)]:
        if queryType == "insert":
            testTreeObj.insert(query)
            plotTree.plotTree(testTreeObj.root, "test.png")
            img = pygame.image.load(os.path.join("test.png"))
            img = pygame.transform.scale(img, (1366, 768))
            img.convert()
            screen.blit(img, (0, 0))
            pygame.display.flip()
            while True:
                event = pygame.event.wait()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return
                    elif event.type == KEYDOWN and event.key == K_RETURN:
                        break

# correctness for TwoThreeTree
correctCases = 0
for queryList in queryLists:
    testTreeObj = testModule.TwoThreeTree()
    TreeObj = sourceModule.TwoThreeTree()
    currentCorrectCases = 0
    currentMaxPossible = 0
    for (i, (queryType, query)) in enumerate(queryList):
        currentMaxPossible += 1/(i+1)
        if queryType == "insert":
            try:
                testTreeObj.insert(query)
                TreeObj.insert(query)
                assert(isIsomorphic(testTreeObj.root, TreeObj.root))
                currentCorrectCases += (1/(i+1))
            #except AssertionError:
            except:
                pass
        elif queryType == "search":
            try:
                assert(testTreeObj.search(query) == TreeObj.search(query))
                currentCorrectCases += (1/(i+1))
            #except AssertionError:
            except:
                pass
    correctCases += (currentCorrectCases)/(currentMaxPossible)

print("TwoThreeTree:", correctCases, "cases passed")
