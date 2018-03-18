* On an unrelated note, the game of Cops and Robbers come to mind. This is a game played on a graph by a cop player and a robber player. The game begins with the cop choosing a vertex on the graph and then the robber choosing a vertex. In each subsequent turns, the robber and the cop take turns moving to a vertex to which there is an edge from their current vertex. The cop wins if he can move to a vertex where the robber is. The robber wins if he can indefinitely avoid the cop.
  * In [this video](https://youtu.be/9mJEu-j1KT0), Kelsey Houston-Edwards gives a very interesting characterization of copwin graphs, the graphs in which the cop has a winning strategy.
  * [Wikipedia](https://en.wikipedia.org/wiki/Cop-win_graph#Recognition_algorithms_and_the_family_of_all_dismantling_orders) discusses some algorithmic approaches on how these graphs can be recognized. As an interesting exercise, you can try implementing them.

* The Strongly Connected Component finding algorithm that you learnt in class is the [Kosaraju's Algorithm](https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm).
  * [Here](http://pythonexample.com/snippet/kosarajupy_agnishom_python) is a quick python implementation of this algorithm.
  * Another algorithm that does the same thing is [Tarjan's Algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm)
    * You can try implementing this.
