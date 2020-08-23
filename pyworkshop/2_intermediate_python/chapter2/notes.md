# Advanced looping

https://www.learnpython.dev/03-intermediate-python/20-advanced-looping/10-list-comprehensions/

## List comprehensions
Sorta similar to the `.map()` and `.filter()` and other array methods in JS.  Convenient powerful shorthands for making lists.

Say you want to iterate through a list, perform an operation on each item that produces a new value, and return a new list with those new values.  You would use `.map()` in JS, but in python you can do a list comprehension.  List comprehensions put an entire expression inside the square brackets: 

```python
names = ['jimmy', 'susan', 'peter']
[name.upper() for name in names] # ['JIMMY', 'SUSAN', 'PETER'] 
```

So the syntax is kind of like: 
```python
[ transform(thing) for thing in list_of_things ]
```

```python
[num * num for num in range(6)] # [0, 1, 4, 9, 16, 25]
```

You can add a conditional filtering mechanism at the end of a list comprehension.  Say you want to do the above squaring operation but only on the even numbers:

```python
[num * num for num in range(6) if num % 2 == 0] # [0, 4, 16]
```

## Set comprehension
Works very similarly for transforming a list into a set

```python
{ num * num for num in range(10) }
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
```

## Dictionary comprehension
Construct a key:value expression in your transformation step to create a dictionary from a list:
```python
{ num: num * num for num }
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Generator expressions (comprehensions)
Generators are iterables that generate values on demand, instead of loading a massive list into memory.  They return a generator, not a list.

Wrap the comprehension expression in parentheses instead of square brackets to make a generator expression.

```python
gen = (x ** 2 for x in range(10) if x % 2 == 0)
type(gen) # <class 'generator'>
```

You can use a generator in place of list in a lot of expressions.  Note that once a generator has been fully iterated, it is now empty and functions as an empty array when used:

```python
gen = (x ** 2 for x in range(10) if x % 2 == 0)
# use the above generator to make a set. each number is computed on the fly
{ v for v in gen } # {0, 64, 4, 36, 16}

max(gen) # ValueError: max() arg is an empty sequence

# reinstantiate generator (important because the above loop ran through the iterator leaving it empty)
gen = (x ** 2 for x in range(10) if x % 2 == 0)
max(gen) # 64
```

Generator are generated when you put them in a comprehension, or a for loop, or when calling `next(generator)` is called.

## Slicing 
Any ordered sequence (list, tuple, or string ) can be sliced.  It's not a method, it's just a special indexing syntax.  You apply the square bracket syntax with `[starting_index: ending_index: step]` where `starting_index` is included by `ending_index` is not.  `step` defaults to 1:

```python
letters = ['a', 'b', 'c', 'd', 'e']
letters[0:2] # ['a', 'b']
letters[1:3] # ['b', 'c']
# when starting index is omitted, it starts from the beginning
letters[:3] # ['a', 'b', 'c']
# when ending index is omitted, it goes to the end
letters[2:] # ['c', 'd', 'e']
letters[-2:] # ['d', 'e']
```

Assigning `new_list = some_list`, we have not created two lists.  We have just created a pointer to `some_list`.  Thus any mutations to `new_list` would also be reflected on `some_list`.  Sometimes you want to clone a list so that you can modify the clone without updating the original.  __Slicing with both indeces omitted does this__

```python
some_list = [1, 2, 3]
a_new_list = some_list[:]
# only modifies `a_new_list`
a_new_list.append(4)
# use a -1 step to clone a list in reverse
reverse_list = some_list(::-1)
# [3, 2, 1]
```

## Zip
You have two different lists, and you want to unify them by index, where the first item in list 1 is grouped with the first item in list 2, etc.  `zip(l1, l2)` does that.
```python
players = ['Susy', 'Alex', 'Roberto']
scores = [88, 78, 92]
zipped = zip(players, scores)
type(zipped) # <class 'zip'>
```

A zip object is kind of like an iterable.  It's not immediately explorable without throwing it in a loop, comprehension, or calling `next(zipped)`.  What you'll see is that each item in the zip iterable is a tuple:

```python
# convert iterable to list to see what's inside
scorecards = list(zip(players, scores))
# [('Susy', 88), ('Alex', 78), ('Roberto', 92)]

# or turn it into a dict
scorecards = list(zip(players, scores))
# {'Susy': 88, 'Alex': 78, 'Roberto': 92}
```