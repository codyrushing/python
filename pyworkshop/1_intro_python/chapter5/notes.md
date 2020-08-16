# Booleans and logic

### Truthiness
Truthiness exists in python, although it's not the same as JS.  To figure out if something is truthy, just pass it into `bool()` to figure it out.
__Falsey__:
* 0
* Empty string
* None
* Empty sequences:
  * []
  * {}
  * ()
  * set()

__Truthy__:
* any non-zero number or non empty string
* any non-empty

### Comparisons
Operators
* `>`, `>=`, `<`, `<=`

String comparison is done by the ascii value of each character.  Capital letters come before (are less than) lower case. `'B' > 'a'` evaluates to false

Comparing sequences is different than JS.  If all of the values are equal and in the same order, two lists are considered equal:
```python
[1, 2, 3] == [1, 2, 3] # True
```
Whereas `==` and `!=` is used to establish equality or non-equality, the `is` keyword is used to establish identity (ie, do they point to the same value in memory)
```python
[1, 2, 3] is [1, 2, 3] # False
```
Those two lists are instatiated separately and occupy differnet places in memory.  Thus they are not equal.

`and`, `or`, `not`
* `and` is kind of like the `{ conditional && <RenderWhenTrue />}` in React.  If the statement to the left of `and` is truthy, we get to the second statement. otherwise, just return the first statement
```python
1 and 'yes' # evaluates to 'yes'
None and 'no' # evaluates to None
[] and {} # evaluates to []
```

* `or` looks at the statement to the left and if it is false, it evaluates to the statement on the right.
```python
0 or 1 # 1
{1} or True # {1}
[] or {} # {}
```

* `not` is just negation. always returns a boolean
```python
not 0 # True
not 'hello' # False
```

