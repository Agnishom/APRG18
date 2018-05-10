import random
import pickle
import sys
from collections import deque

sys.setrecursionlimit(10000)

def countIslands(grid):
    grid = grid.split()
    explored = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and (not explored[i][j]):
                islands += 1
                stack = [(i, j)]
                while len(stack) > 0:
                    ci, cj = stack.pop()
                    if explored[ci][cj]:
                        continue
                    explored[ci][cj] = True
                    for (di, dj) in [(1,1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
                        try:
                            if (0 <= ci + di < len(grid)) and (0 <= cj + dj < len(grid[0])):
                                if (not explored[ci+di][cj+dj]) and (grid[ci+di][cj+dj] == '1'):
                                    stack.append((ci+di, cj+dj))
                        except:
                            print(i, j, di, dj)
    return islands

def sequenceJump(markings):
    N = len(markings)
    stoneLocations = dict()
    for (i, val) in enumerate(markings):
        if val in stoneLocations:
            stoneLocations[val].append(i)
        else:
            stoneLocations[val] = [i]
    adjList = [[] for _ in markings]
    for i in stoneLocations:
        for v in stoneLocations[i]:
            for u in stoneLocations[i]:
                adjList[v].append(u)
                adjList[u].append(v)
    for i in range(1, N-1):
        adjList[i].append(i+1)
        adjList[i].append(i-1)
    adjList[0].append(1)
    adjList[N-1].append(N-2)
    queue = deque([(0,0)])
    visited = [False]*N
    while True:
        (cur, dist) = queue.popleft()
        if cur == N-1:
            return dist
        visited[cur] = True
        for neighbor in adjList[cur]:
            if not visited[neighbor]:
                queue.append((neighbor, dist + 1))

def countBridges(vertexCount, adjList):
    visited = [False for i in range(vertexCount+1)]
    depth = [0 for i in range(vertexCount+1)]
    low = [0 for i in range(vertexCount+1)]
    parent = [0 for i in range(vertexCount+1)]
    bridges = 0
    def rec(u, d):
        nonlocal bridges
        visited[u] = True
        depth[u] = d
        low[u] = d
        childCount = 0
        for v in adjList[u]:
            if not visited[v]:
                parent[v] = u
                rec(v, d+1)
                childCount += 1
                low[u] = min(low[u], low[v])
                if low[v] > depth[u]:
                    bridges += 1
            elif v != parent[u]:
                low[u] = min(low[u], depth[v])
    for u in range(1, len(adjList)):
        if not visited[u]:
            rec(u,1)
    return bridges

countIslandCases = []
for _ in range(10):
    gridSize = random.randint(1,1000)
    randomGrid = "\n".join(["".join(['0' if random.random() > 0.5 else '1' for _ in range(gridSize)]) for _ in range(gridSize)])
    answer = countIslands(randomGrid)
    countIslandCases.append((randomGrid, answer))

countBridgesCases = []
for _ in range(10):
    graphSize = random.randint(1, 1000)
    newGraph = dict(zip(range(1,graphSize+1), [[] for i in range(graphSize)]))
    for i in range(1, graphSize+1):
        for j in range(i+1, graphSize+1):
            if random.random() < 0.5:
                newGraph[i].append(j)
                newGraph[j].append(i)
    nBridges = random.randint(1, int(0.5 * graphSize))
    bridgePoints = sorted(random.sample(range(1, graphSize-1), nBridges))
    for u in bridgePoints:
        for i in range(1, graphSize+1):
            newGraph[i] = list(filter(lambda x: x <= u,newGraph[i]))
        newGraph[u].append(u+1)
        newGraph[u+1].append(u)
    perm = list(range(1,graphSize+1))
    random.shuffle(perm)
    perm = [0] + perm
    graph = dict()
    for v in newGraph:
        graph[perm[v]] = list(map(lambda x: perm[x], newGraph[v]))
    answer = countBridges(graphSize, graph)
    countBridgesCases.append(((graphSize, graph), answer))

sequenceJumpCases = []
for _ in range(10):
    seenSoFar = set([random.randint(1,2018)])
    newSequence = []
    sequenceLength = random.randint(1, 1000)
    for i in range(sequenceLength):
        if random.random() < 0.4:
            n = random.randint(1, 2018)
            newSequence.append(n)
            seenSoFar.add(n)
        else:
            newSequence.append(random.sample(seenSoFar,1)[0])
    answer = sequenceJump(newSequence)
    sequenceJumpCases.append((newSequence, answer))




cases = {"countIslandCases": countIslandCases, "countBridgesCases": countBridgesCases, "sequenceJumpCases": sequenceJumpCases}
pickle.dump(cases, open("cases.dat", "wb"))
