* Another interesting algorithm for computing the Minimum Spanning Tree that you may not have seen is [Boruvka's Algorithm](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)

* A related concept is the minimum cost _arborescence_ which is a generalization of this idea in a directed graph.
  * See [Edmond's Algorithm](https://en.wikipedia.org/wiki/Edmonds%27_algorithm), which finds such structures.

* In both the algorithms above, there is a notion of contracting a connected component of a graph into a supernode. I am not very sure of what a good way to implement this would be. If you do, please let me know, or [answer my stackoverflow question](https://stackoverflow.com/questions/49597647/how-does-one-implement-graph-algorithms-that-require-efficient-contraction-and-e).

* Suppose a graph has distinct weight for every edge. Show that the minimum spanning tree is unique.

* An interesting application of Prim's Algorithm is to [generate mazes](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm)

* Given a graph, how do you sample a spanning tree uniformly at random from the set of all spanning trees?
  * Notice that a brute force approach might be very expensive since there could be a superexponential number of them
    * [Check out Cayley's Formula](https://en.wikipedia.org/wiki/Cayley%27s_formula)
  * However, [Wilson's Algorithm](https://en.wikipedia.org/wiki/Loop-erased_random_walk) let's you do this in a farely efficient way.
    * It's oddly satisfying watching the algorithm in action: [Link](https://www.reddit.com/r/Python/comments/5dxhp9/wow_guy_i_made_an_awesome_gif_animation_of/)
