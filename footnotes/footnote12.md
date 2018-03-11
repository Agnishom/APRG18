* You may have learnt that you could implement depth-first search using either a stack or using recursion.
  * Do they necessarily visit the vertices in the same order?
    * [Here](https://en.wikipedia.org/wiki/Depth-first_search#Pseudocode) is a counterexample.

* Some interesting applications of DFS are as follows:
  * [Finding Articulation Points](https://en.wikipedia.org/wiki/Biconnected_component#Equivalence_relation): Vertices in the graph which when removed increases the number of connected components
  * [Finding Bridges](https://tanujkhattar.wordpress.com/2016/01/10/the-bridge-tree-of-a-graph/): Edges in the graph which when removed increases the number of connected components.
  * Given a graph, and two vertices \(u\) and \(v\), are there two paths from \(u\) to \(v\) that do not have vertices in common? How can you find them?

* A Mandatory xkcd reference.
  ![A breadth-first search makes a lot of sense for dating in general, actually; it suggests dating a bunch of people casually before getting serious, rather than having a series of five-year relationships one after the other.](https://imgs.xkcd.com/comics/dfs.png)
