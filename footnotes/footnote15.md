* Dijkstra's Algorithm requires you to pick the node which has not yet been marked and has the least estimated distance so far. How do you do this?
  * Need a _heap_ - a data structure to figure out the element with the lowest priority so far.

* Can Dijkstra's Algorithm be used on graphs with negative edge weights?
  * Spoiler Alert: No!
    * But why not?
  * Meet [Bellman-Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)

* BFS explores equally in all directions, Dijkstra's lets you prioritize by edge weights. But can we modify the path finding algorithm so as to reach a specific destination if we have a heuristic distance in mind?
  * [Redblob Games](https://www.redblobgames.com/pathfinding/a-star/introduction.html) has a nice introduction to A* search, along with an [implementation guide](https://www.redblobgames.com/pathfinding/a-star/implementation.html).
