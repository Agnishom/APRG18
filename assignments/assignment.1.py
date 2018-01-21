def kNacci(k, seeds, n):
    # k is an integer
    # seeds is a list of k values, kNacci(0), kNacci(1), ... kNacci(k-1)
    # you have to return kNacci(k, seed, n)
    return ...

def matrixMultiply(M, N):
    # M and N are matrices such that their product is well-defined
    # you have to return their product
    return ...

def selectLeader(N, k):
    # N is the number of people in the simulation
    # k is the constant as described in the problem statement
    # you should return the run of game, as a list of lists
    return ...

def representable(B, n):
    # B is the number described in the problem
    # n is the number you are testing for
    # you should return a boolean indicating if the number is present
    return ...

def main():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = [[19, 22], [43, 50]]
    print("A*B == C: ", matrixMultiply(A,B) == C)
    print("kNacci(2, [0,1], 20) == 6765: ", kNacci(2, [0,1], 20) == 6765)
    selectLeaderRun = [[1,2,3,4,5],[2,3,4,5],[2,4,5],[2,4],[2]]
    print("selectLeader(5, 2) == selectLeaderRun: ", selectLeader(5, 2) == selectLeaderRun)
    print("not representable(3, 6): ", not representable(3, 6))
    print("representable(3, 40): ", representable(3, 40))

if __name__ == "__main__":
    main()