# Iteration
You usually don't need a traditional `for(i=0; i<arr.length; i++)`, python has better loop utilities.

### Looping over sequences/collections

Looping a list, use `for in`:
```python
colors = ['red', 'green', 'blue']
for color in colors:
  print(color)
```

If you need an index in your loops, you can use `enumerate(loop)` which will return a list of tuples that are `(index, item)`
```python
for i, color in enumerate(['red', 'green', 'blue']):
  print(f"index: {i}, color: {color}")
```

### Iterating over a count
`range()` is a handy method that returns a list of integers, you can use it to create loops that run n number of times or to create a list of indeces:
```python
for num in range(0, 5): # will print 0 through 4
  print(num)
```
the range arguments are the first number to start and the number before which to stop, (so that number is not included)
```python
for num in range(1, 4): # will print 1 through 3
  print(num)
```
it also accepts a step parameter as its third argument
```python
for num in range(1, 7, 2): # will print 1, 3, and 5
  print(num)
```

### Iterating over a dictionary
Best to use `some_dict.items()`, which returns a list of tuples.  because each item in the items array is a tuple, it can be unpacked or destructured in the for statement

```python
colors = { 'red': '#f00', 'green': '#0f0', 'blue': '#00f' }
for label, hex in colors.items():
  print(label, hex)
```

### While loops
```python
counter = 0
max = 4
while counter < max:
  print(f"The count is {counter}")
  counter = counter + 1
```