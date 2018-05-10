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

# correctness for matrix multiplication
def mm(A, B):
    return [[sum(x * B[i][col] for i,x in enumerate(row)) for col in range(len(B[0]))] for row in A]

correctCases = 0
for currentCase in cases['matrixCases']:
    d1, d2, d3 = currentCase['d1'], currentCase['d2'], currentCase['d3']
    A = currentCase['A']
    B = currentCase['B']
    try:
        assert(mm(A, B) == testModule.matrixMultiply(A, B))
        correctCases += 1
    except:
        print("Matrix Multiplication Failed")
        print(A, B)

print("matrixMultiply:", correctCases, "cases passed")

# correctness for kNacci
def kNacci(k, seeds, n):
    if n < k:
        return seeds[n]
    else:
        workArray = seeds + [0]*(n-k+1)
        for i in range(k, n+1):
            workArray[i] = sum(workArray[i-k: i])
    return workArray[n]

correctCases = 0
for currentCase in cases['kNacciCases']:
    k, n = currentCase['k'], currentCase['n']
    seeds = currentCase['seeds']
    try:
        assert(kNacci(k, seeds, n) == testModule.kNacci(k, seeds, n))
        correctCases += 1
    except:
        print("kNacci Failed")
        print(k, seeds, n)
print("kNacci:", correctCases, "cases passed")

#correctness for representable
def representable(B, n):
    A = set([1])
    old = A
    for _ in range(int(math.log(n, B)) + 1):
        new = set()
        for m in old:
            for j in range(B-1):
                new.add(m*B + j)
        old = new
        A = A.union(old)
    return (n in A)

correctCases = 0
for currentCase in cases['representableCases']:
    B, n = currentCase['B'], currentCase['n']
    try:
        assert(representable(B, n) == testModule.representable(B, n))
        correctCases += 1
    except:
        print("representable Failed")
        print(B, n)
print("representable:", correctCases, "cases passed")

#correctness for selectLeader
def selectLeader(N, k):
    run = []
    soFar = collections.deque(list(range(1,N+1)))
    while True:
        run.append(sorted(list(soFar)))
        if len(soFar) <= 1:
            break
        soFar.popleft()
        soFar.rotate(-(k-1))
    return run

correctCases = 0
for currentCase in cases['selectLeaderCases']:
    N, k = currentCase['N'], currentCase['k']
    try:
        assert(selectLeader(N, k) == list(map(sorted,testModule.selectLeader(N, k))))
        correctCases += 1
    except:
        print("selectLeader Failed")
        print(N, k)
print("selectLeader:", correctCases, "cases passed")
