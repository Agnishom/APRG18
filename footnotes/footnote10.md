* There are two popular representations of graphs on the computer:
  * **Adjacency Matrix:** This is a matrix whose rows and columns represent vertices and the entry `[i][j]` of the matrix denotes if there is an edge from vertex `i` to vertex `j`.
  * **Adjacency List:** In this representation, along with every vertex, you keep a list of all it's neighbors.
  * Other possible ways to represent graphs could be **Edge Lists** or **Incidence Matrices**.

* Which representation you should pick depends on what graph algorithm you need to implement.
  * Which format is faster when you intend to implement breadth first search?
  * How do you represent graphs which are directed? What if the vertices are labelled? What if the edges are weighted?

* How do you represent graphs in functional languages?
  * The above methods might work, but are not aligned to the functional style and there is a trade off between elegance and speed when you choose to use them.
  * Two interesting approaches I have heard of are:
    * [Inductive Graphs](https://web.engr.oregonstate.edu/~erwig/papers/InductiveGraphs_JFP01.pdf)
    * [Algebraic Graphs](https://github.com/snowleopard/alga-paper)
  * If you are interested in contributing along these lines, check out [Summer of Haskell](https://summer.haskell.org/ideas.html#graphs)

* Check out [Hackerrank](https://www.hackerrank.com/domains/algorithms/graph-theory?filters=difficulty%3Amedium) for some introductory graph theory programming problems.
  * If you want some really hard graph theory problems, check out [Daniel Ploch's Lost Woods](https://brilliant.org/profile/daniel-9etuk9/sets/the-lost-woods/?ref_id=1090390)
  * On a totally unrelated note, check out their [2018 Developer Skills Report](https://research.hackerrank.com/developer-skills/2018/)

* How would you use breadth first search to:
  * figure out the shortest path from a given node on a graph to another given node?
  * find out the number of connected components in a graph?

* You could possibly use [lists as queues](https://docs.python.org/3.1/tutorial/datastructures.html#using-lists-as-queues) in python, but the python documentation says that lists are not really optimized this.
  * Use `from collections import deque` to get a double ended queue instead.
