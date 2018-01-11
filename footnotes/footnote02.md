* In light of the discussion about the strange behaviour with variable assigment, we could look at these two questions:
  * It's a better idea to think of python variables as references, rather than pointers: [Link](https://stackoverflow.com/questions/13530998/python-variables-are-pointers)
  * [Immutable vs Mutable Types](https://stackoverflow.com/a/8059504/1955231)

* Courtesy of Kapil, here is a piece of code; can you figure out what it does?
  * Also notice that in python, unlike in Haskell, functions are really procedures, they have side effects and are not pure.

```
y = 7
l = [7]
m = [7]
n = l
def f(l, m, n, y):
  y = 9
  l[0] = 9
  m = [9]
  n[0] = 10
print(l, m, n, y)
```

* Consider this code. What is it's behaviour?
  * Write a snippet of code that does not have this issue and has the intended behavior.

```
l = [[0]*2]*2
l[0][0] = 1
print(l)
```

* We have [list comprehensions in python](https://docs.python.org/3.6/tutorial/datastructures.html#list-comprehensions). For example, what do you think this list is? `[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]`
  * We also have genexp's, which are basically lazy lists, i.e, they do not occupy full memory when used. For example,
  ```
  for (x,y) in ((x, y) for x in [1,2,3] for y in [3,1,4] if x != y):
    print(x,y)
  ```

* You should briefly take a look at [tuples](https://docs.python.org/3.6/tutorial/datastructures.html#tuples-and-sequences), [sets](https://docs.python.org/3.6/tutorial/datastructures.html#sets) and [dictionaries](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries)
