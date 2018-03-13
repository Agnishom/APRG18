* How can you check algorithmically if a given graph is a DAG?

* There is actually a [quiet straightforward way](https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search) to think of a topological sorting in terms of a DFS.
  * A topological sorting orders the vertices of the DAG in descending order of their leaving time.

* We have mentioned that counting the number of linear orderings of a graph is a [difficult problem](https://mathoverflow.net/questions/45875/how-can-you-compute-the-number-of-topological-sorts-in-a-dag).
  * A brute force approach might be to try all possible vertices with in-degree 0. However, this approach can become quiet inefficient. Can you find a graph of size \(n\) which has at least \(2^n\) topological orderings?

* On a programming note, you may have seen this line in your assignments, or on the internet:
  ```
  if __name__ == "__main__":
    main()
  ```
  * [What do you think it does?](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
