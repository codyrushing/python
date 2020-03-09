### Functions

```python
def add_numbers(x, y):
	return x + y;
```

Functions without default arguments are required.  If you tried to call the function without those, it will syntax error.

To be explicit, you can pass in your arguments with labels:

```python
add_numbers(x=2, y=4)
# equivalent to
add_number(2, 4)
# you can also change the order around if they're labeled
add_number(y=3, x=1)
```

This is an improvement over JS because order can be arbitrary, which is why JS functions so often use a single object as their sole argument

Do not use a mutable type as a default argument.  For example, consider this function that has a default argument of an empty list:

```python
def add_item(item, collection=[]):
	collection.append(item)
	return collection
```

If you call this function, the variable of collection gets set, __but then it persists for later calls__.  It doesn't get reinstantiated for each call, unlike JS.  So never do that.

```python
add_item('a')
# ['a']
add_item('b')
# ['a', 'b']
```

A better way to implement this function would be a simple None check

```python
def add_item(item, collection=[]):
	if collection is None:
			collection = []
	collection.append(item)
	return collection
```

### Scope

Scope works similar to JS.  A function creates a separates scope.  It can access variables of its parent scope, but the parent scope can not access a variable created by the function.  __However, a function can not mutate variables from a parent scope__.  The mutations will reflect __only inside the function__.  Basically, a function can't rewrite a global variable.  This is why global variables in python should probably only be constants that never change.

### Mechanics
Indentation is the `{}` of python.  A line ending with `:` signals that the next line should be indented

A `\` at the end of a line indicates a continuation.  It is a way to break expressions up visually and keep there from being too much on a line:

```python
some_list = ['a', 'b', 'c', \
	'd', 'e', 'f',
	'g', 'h', 'i'
	]
```

semi colons do the opposite, they combine multiple statements on a single line:
```python
a = 1; b = 2; c = 3;
```