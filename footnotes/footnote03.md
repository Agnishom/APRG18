* [Here](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops) are some more control flow statements which come in handy.
  * `break`, breaks out of the innermost loop.
  * `else` clause on loops: this clause is executed only when the loop goes through without encountering a `break`
    ```
    for n in range(2, 10):
      for x in range(2, n):
          if n % x == 0:
              print(n, 'equals', x, '*', n//x)
              # we already know that n is not a prime
              # no need to check for other n's
              break
      else:
          # loop fell through without finding a factor
          print(n, 'is a prime number')
    ```
  * `continue`, skips the current iteration of the loop and goes to the next iteration.
      ```
      while True:
           option = input("Say YES or NO: ")
           if option not in ["YES", "NO"]:
                   continue
           if option == "YES":
                   print("You said YES")
           else:
                   print("You said NO")
           break
      ```

* Because you saw `filter`s, and `map`s:
  * We can also have `fold`, which is available from [`functools.reduce`](https://docs.python.org/3.6/library/functools.html).
  * We can also have `lambda` functions. E.g, `square = lambda x : x * x` in python is the same as `square = (\x -> x*x)` in Haskell.

* You saw how to call the constructors of several types to convert between types. Here is a nice trick that removes duplicates in a list.
  ```
  removeDuplicates = lambda l: list(set(l))
  ```
