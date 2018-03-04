* A [chordal graph](https://en.wikipedia.org/wiki/Chordal_graph) is one where there are which all cycles of four or more vertices have a chord.
  * Try proving the following interesting characterization of Chordal graphs from Wikipedia:
    > A perfect elimination ordering in a graph is an ordering of the vertices of the graph such that, for each vertex v, v and the neighbors of v that occur after v in the order form a clique. A graph is chordal if and only if it has a perfect elimination ordering.

  * An interesting variant of Breadth First Search, known as [Lexicographic Breadth-First Search](https://en.wikipedia.org/wiki/Lexicographic_breadth-first_search) can help find such perfect elimination orderings. [Here](https://en.wikipedia.org/wiki/Lexicographic_breadth-first_search#Chordal_graphs) is a short explanation of that.
  * As an exercise, try implementing this whole method of recognizing chordal graphs in python.

* An Eulerian Tour on a graph is a ordering of the vertices that uses each edge exactly once.
  * You may have learnt an interesting characterization of graphs with Eulerian Tours in a different course. But how do you actually find an Eulerian Tour?
  * [Here](https://stackoverflow.com/a/27996779/1955231) is a very nice algorithm to do this.
    * Prove that this algorithm is correct.
    * How much time does this algorithm take?
    * Implement this algorithm.

* Given a graph, can you find its BFS tree? (Implement this)
  * [Given the spanning tree of a graph, can you tell if it is a BFS tree of the graph?](https://github.com/Agnishom/IOITC16/blob/master/tst/Day1/BFSTree/BFSTree/BFSTree.pdf)
