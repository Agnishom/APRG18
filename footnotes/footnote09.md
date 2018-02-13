* While we are on the topic of sorting, let's examine some out of the box sorting algorithms.
  * [Humor]
    * **Bogosort:** (Average Running Time: O(n!)) Shuffle the array. Check if the array is sorted. If yes, stop, otherwise, repeat.
    * **Quantum Bogosort:** (Worst Case Running Time: O(1)) Shuffle the array. If yes, stop, otherwise, destroy the universe.
    * [**Sleeping Sort:**](https://stackoverflow.com/questions/6474318/what-is-the-time-complexity-of-the-sleep-sort) (Worst Case Running Time: O(max(input)+n)) For each number `i` in the array, spawn a thread that sleeps for `i` seconds and then prints `i`. At the end of `max(input)` seconds, the elements of the array would be printed in sorted order.
  * [Sorts that can be parallelized]
    * **Bitonic Sort:** (Work: O(n log(n)^2), Span: O(log(n)^2)) The idea behind this sort is to use bitonic sequences, which are sequences which are first increasing and then decreasing. The algorithm proceeds as follows:
      1. Recursively sort half of the list to be ascending, and the other half to be descending. And then merge these two lists.
      2. To merge two lists, for every element in the left list, find the corresponding element in the right list and swap it, if necessary, to make sure that the element on the left list has the smaller elements. This would give rise to another bitonic sequence (why?), which we would split into two sequences and merge again.
      * You could watch this sort videos that explain this idea: [Video 1](https://www.youtube.com/watch?v=rZyqw8BdkgQ), [Video 2](https://www.youtube.com/watch?v=6v_D0X15jf0), [Video 3](https://www.youtube.com/watch?v=9hE9YrnbfbY), [Video 4](https://www.youtube.com/watch?v=3535fVGDdq4)
      * How do you think this algorithm can be parallelized?
    * **Odd Even Bubble Sort:** (Work: O(n^2), Span: O(n)) Roughly the algorithm that I suggested [here](https://github.com/Agnishom/PRGH17/blob/06243c803f2ac1d636809a09c0c697af77a89849/footnotes/footnote11.md)
  * [Other Misscleanous Sorts]
    * **Pancake Sorting:** On a frying pan, you have a stack of pan cakes, of different radii. You intend to arrange them in a way such that the smallest pancake is in the top, the largest is at the bottom. However, the only move you are allowed is that you could insert your spatula at any point in the stack and invert the stack of pancakes above that point. Can you use this operation repeatedly to sort the pancakes?
      * ![What you are allowed to do](https://upload.wikimedia.org/wikipedia/commons/0/0f/Pancake_sort_operation.png)
    * **Counting Sort:** Suppose there are a large number of students who are the students of a Massive Online Open Course. However, they have all taken a test, which assigns them some marks which is within 0 to 5 inclusive. The instructor wants to sort the students based on this marks. Can he do this in linear time?
      * In other words, if the values in an array are from a small set, can we beat the O(n log(n)) bound?
