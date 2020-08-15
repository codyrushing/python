### Lists
* Several built-in methods that are not part of the list object, but are just globally available utilities
  * eg. `len()`

#### Sorting
* `sorted()` will try sort a list and return a copy of that list sorted.  it applies natural sorting for lists of sortenumbers and alphabetical for strings.  if you mix types, you could get an error
* `l.sort()` - a method on the list instance. does the same kind of sorting as `sorted()`, but in place, so the original list is modified

#### More list methods
* `insert(position, value)` - insert `value` at `position` index
* `l1.extend(l2)` - concats `l2` onto `l1` and modifies `l1`
* Searching
  * `value in l1` - returns a boolean if `value` is in l1
	* `l1.index(v)` - gets the index of `v`, if not found, it will error
	* `l1.count(v)` - gets the number of time `v` occurred, if not found, it will return 0
* `l1.remove(v)` - removes an item. if multiple matching items are found, only the first will be removed
* `l1.pop()` - remove the last item.  accepts an argument of which index to remove, defaults to last item

### Tuples
* kind of like an immutable list. once they are instantiated, they can't be modified.  this is helpful if you want to create something with a guaranteed structure.  Maybe used as a return type for a function that needs to return a fixed amount of multiple values.  they're a good way to quickly consolidate some information and make it constant.  Or like a fixed schema, for example from a CSV or spreadsheet.
* The shorthand for creating a tuple is `(v1, v2, v3)` or `v1, v2, v3`.  Note that if you try to instantiate a tuple with a single item like `(v1)`, that won't work because the interpreter will try to make that a logical grouping instead.  You would have to do `(v1,)` to make a tuple.
* values can be access with index just like lists.  You can also unpack them, which is sort of like destructuring in JS
```python
student = ("Timmy", 12, "Math", 3.8)
# unpack the tuple, create a variable for each value
name, age, favorite_subject, gpa = student
# name == "Timmy"
```
* You must unpack all items in the tuple, or you will get an error
* They're easy to use as function returns
```python
def get_http_request():
	return 200, 'OK'
status_code, name = get_http_request()
```

### Sets
[https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/50-sets/](https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/50-sets/)

Sets are collections where order is __not__ preserved and all members are unique.  Searching through sets is faster than lists.  Because order is not preserved, you can not access by index.  They're contents are hashed, which is why searching is fast, but as such, you can not have mutable data types inside of a set.  Mutable types are not hashable, which you can verify by trying to call `hash([])` which will throw an error.  So if you try to put a mutable type like a list in a set, you will get an error.  Sets are useful for de-duping a list, tuple or other container type.
```python
names = {'John', 'Jacob', 'John'} # shorthand declaration
len(names) # 2
# sets can be instatiated with lists or tuples using the non-shorthand declaration
foods_set = set(['pizza', 'burger', 'noodles'])
# using shorthand to make an empty set actually makes an empty dict, so be careful. use `set()` to make an empty set
empty_set = {}
type(empty_set) # <class 'dict'>
```
* `s.add(item)` - adds item to set
* `s.remove(item)` - removes item from set
* `s.discard(item)` - just like `remove` but it will not throw an error if item is not in the set
* `s.update(seq)` - concats `seq` onto `s` in place.  this method always expects a sequence (list, tuple, or set).  It will try to turn any item you pass it into a sequence.  If you pass it a string, it will add each character in the string to the set.  If you pass it a dict, it will add the keys from the dict.  Probably just wanna stick to lists, tuples, or sets.  
* `item in s` - checks whether set `s` contains `item`
* Union: `s1.union(s2)` or `s1 | s2`
	* returns a new set with `s1` and `s2` concated
* Intersection

