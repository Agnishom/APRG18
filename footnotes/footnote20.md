* Many of you implemented `kNacci` in the first assignment directly using recursion. Having done a module on dynamic programming, do you see what the issue is and how you could have fixed it?
  * Actually, [there is a way](https://brilliant.org/wiki/fast-fibonacci-transform/) to caculate fibonacci numbers in logarithmic time.
  * Chebyshev Polynomials of the first kind are polynomials which satisfy `T[n](x) = cos(n * arccos(x))`, for a specific `n`.
    * For example, `T[3](x) = 4x^3 - 3x` since `cos(3x) = 4 cos(x)^3 - 3 cos(x)`
    * Determine a recurrence relation for `T[n]` using `T[n-1]` and `T[n-2]`
    * Use the recurrence above to give an algorithm to find `T[n]` in linear time.
    * There is a faster way to compute `T[n]`. Can you find it?

* What do you think is the distinction between dynamic programming and divide and conquer?

* There is a rich collection of classic problems that can be solved with dynamic programming:
  * [IARCS Study Material](https://www.iarcs.org.in/inoi/online-study-material/topics/dp.php)
  * [GeeksForGeeks](https://www.geeksforgeeks.org/dynamic-programming/)
  * [CodeMonk - HackerEarth](https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/)
  * [Brilliant](https://brilliant.org/practice/dynamic-programming-level-5-challenges/)


* Actually, you may check out [UVA Judge](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=638) for a collection of problems sorted by paradigms with which they could be attacked.
