* For most of this course, we shall use [Python 3](https://www.python.org/) to illustrate programming principles and algorithms. Please install it on your local machine, if you have not already.
  * Another nice way to run python code is to use [repl.it](https://repl.it/repls/OrganicLankyFulmar)
  * If you are not familiar with the python language, and want to jump start, the [official python tutorial](https://docs.python.org/3/tutorial/index.html) is a great resource.

* In the beginning of the last lecture, we emphasized the distinction between the procedural and the functional style. However, [there are a few nice things that we saw in functional programming](https://docs.python.org/2/howto/functional.html) that can still be used in python
  * Functions are still first class. We can still have higher order functions. So, we still have `map`, `filter`, `fold` (called `reduce` in Python), etc
  * Objects that behave like infinite lists (known as `generators`).
  * Lambda functions.

* That said, while you can adopt the functional style in python, there is no way to enforce it. Also, there are no static types here; this means (in some people's opinion) the interpreter would not know if there is a serious nonsensical expression, like maybe applying a function to itself `f(f)` until the interpreter runs the statement and goes into trouble.

* Consider the following snippet of code in Python, which switches the values two variables are holding
  ```
  a = 1
  b = 2
  a, b = b, a
  print(a, b)
  ```
  * Now, contrast this with the following code
    ```
    a = 1
    b = 2
    a = b
    b = a
    print(a, b)
    ```
    * Are the behaviour of these programs the same?
  * Moral: the `=` behaves like an assignment operator, and does not really stand for definitions. Unlike Haskell, variables here are mutable.

* Modify (as much as you like) the `factors` function that you saw in the lecture to create a function `isPrime` that checks if the input is a prime integer.
  * Analyze your program, and try to figure out what sort of control flow (or other) features you may be able to use to make your program better.
