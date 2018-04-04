* The right way to implement checking whether two things are already in a connected component in [Kruskal's Algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) is to use [Union-Find](https://brilliant.org/wiki/disjoint-set-data-structure/)
  * The amortized cost of operations in the Disjoint-Set data structure is not constant, but [grows really really slow](https://en.wikipedia.org/wiki/Ackermann_function#Inverse). To quote Wikipedia, "The function has value < 5 for any value that can be written in the physical universe"

* [Matroids](https://en.wikipedia.org/wiki/Matroid#Greedy_algorithm) are mathematical objects which capture structures on which greedy algorithms can be efficiently used.
  * A related concept is the [Greedoid](https://en.wikipedia.org/wiki/Greedoid).

* There are several kinds of coins in supply `c[0..n-1]`, and you want to find a representation of an amount `v` using as few coins as possible.
  * [When does a greedy algorithm solve this problem?](https://cs.stackexchange.com/questions/6552/when-can-a-greedy-algorithm-solve-the-coin-change-problem)
