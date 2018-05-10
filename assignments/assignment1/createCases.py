import random
import pickle

matrixCases = []
for _ in range(10):
    newCase = {}
    newCase['d1'], newCase['d2'], newCase['d3'] = (random.randint(2, 50) for _ in range(3))
    newCase['A'] = [[random.randint(-100, 100) for _ in range(newCase['d2'])] for _ in range(newCase['d1'])]
    newCase['B'] = [[random.randint(-100, 100) for _ in range(newCase['d3'])] for _ in range(newCase['d2'])]
    matrixCases.append(newCase)


matrixCases.extend([{'d1': 1, 'd2': 1, 'd3': 1, 'A': [[0]], 'B': [[0]] },
                   {'d1': 1, 'd2': 2, 'd3': 1, 'A': [[1, 2]], 'B': [[1], [2]]},
                   {'d1': 2, 'd2': 2, 'd3': 2, 'A': [[1, 2], [3, 4]], 'B': [[1,2], [3,4]]}])

kNacciCases = []
for _ in range(10):
    newCase = {}
    k, n = (random.randrange(2, 50) for _ in range(2))
    seeds = [random.randrange(-100, 100) for _ in range(k)]
    newCase['k'], newCase['n'], newCase['seeds'] = k, n, seeds
    kNacciCases.append(newCase)

kNacciCases.extend([{'k': 1, 'n': 2018, 'seeds': [2017]},
                   {'k': 1, 'n': 0, 'seeds': [0]},
                   {'k': 5, 'n': 5, 'seeds': [5, 4, 3, 2, 1]}])

representableCases = []
for _ in range(10):
    newCase = {}
    B, n = (random.randrange(2, 50) for _ in range(2))
    newCase['B'], newCase['n'] = B, n
    representableCases.append(newCase)

representableCases.extend([{'B': 2017, 'n': 1}])

selectLeaderCases = []
for _ in range(10):
    newCase = {}
    N, k = (random.randrange(2, 50) for _ in range(2))
    newCase['N'], newCase['k'] = N, k
    selectLeaderCases.append(newCase)

selectLeaderCases.extend([{'N': 1, 'k': 2},
                         {'N': 2, 'k': 1},
                         {'N': 1, 'k': 1},
                         {'N': 2, 'k': 2}])

cases = {'matrixCases': matrixCases, 'kNacciCases': kNacciCases, 'representableCases': representableCases, 'selectLeaderCases': selectLeaderCases}
pickle.dump(cases, open("cases.dat", "wb"))
