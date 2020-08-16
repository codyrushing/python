### Lists
* Several built-in methods that are not part of the list object, but are just globally available utilities
  * eg. `len()`

#### Sorting
* `sorted()` will try sort a list and return a copy of that list sorted.  it applies natural sorting for lists of sortenumbers and alphabetical for strings.  if you mix types, you could get an error
* `l.sort()` - a method on the list instance. does the same kind of sorting as `sorted()`, but in place, so the original list is modified

#### More list methods
* `l.append(item)` - pushes an item onto the end of a
* `insert(position, value)` - insert `value` at `position` index
* `l1.extend(l2)` - concats `l2` onto `l1` and modifies `l1`
* Searching
  * `value in l1` - returns a boolean if `value` is in l1
	* `l1.index(v)` - gets the index of `v`, if not found, it will error
	* `l1.count(v)` - gets the number of time `v` occurred, if not found, it will return 0
* `l1.remove(v)` - removes an item. if multiple matching items are found, only the first will be removed
* `l1.pop()` - remove the last item.  accepts an argument of which index to remove, defaults to last item.  This is the preferred way to delete items from an array.

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

Sets are collections where order is __not__ preserved and all members are unique.  Searching through sets is faster than lists.  Because order is not preserved, you can not access by index.  Their contents are hashed, which is why searching is fast, but as such, you can not have mutable data types inside of a set.  Mutable types are not hashable, which you can verify by trying to call `hash([])` which will throw an error.  So if you try to put a mutable type like a list in a set, you will get an error.  Only use sets with immutable data types.  Sets are useful for de-duping a list, tuple or other container type.  not sortable, ordering is never preserved in a set
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
* `item in s` - checks whether set `s` contains `item`.  returns a boolean

* Union: 
	* `s1.union(s2)` or `s1 | s2` (what is in either s1 or s)
	* returns a new set with `s1` and `s2` concatenated, sort of
* Intersection: 
	* `s1.intersection(s2)` or `s1 & s2` (what is in both s1 and s2)
	* returns a new set with only the items that are in both.  opposite of difference
* Difference:
	* `s1.difference(s2)` or `s1 ^ s2`
	* returns a set with elements that appear in only one of the lists.  opposite of intersection

There is something called a `frozenset` type, which is set that is completely immutable.  has all of the non-mutative methods as `set`.

### Dictionaries
[https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/60-dictionaries/](https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/60-dictionaries/)

Key value pairs.  Useful when you want to be able to quickly access data associated with a key, or name.  Dictionaries themselves are mutable, but their keys must be immutable types.  Same as items in sets, keys in dictionaries must be hashable, meaning immutable types.  Values can be mutable types.

Accessing items in a dictionary can be done two different ways:
* by key: `some_dict['key_that_does_not_exist']` - accessing a key directly is fine if the key exists.  if not, error is thrown
* `.get()`: `some_dict.get('key_that_may_or_may_not_exist', None)`.  Falls back to `None` if key is not found, no error.  This is usually better

New keys can be added whenever, and existing keys can be reset.  Just like JS.

Searching:
`'key_name' in some_dict`: returns a boolean

Manipulation:
`s1.update(s2)` - merge in-place s2 into s1

* `some_dict.keys()`: returns a list of all keys
* `some_dict.values()`: returns a list of all values
* `some_dict.items()`: returns a list of tuples. in each tuple, the first item is the key and the second is a value:
	```python
	{'a': 1, 'b': 2, 'c': 3}.items() # dict_items([('a', 1), ('b', 2), ('c', 3)])
	```

## Advanced
List slicing can be done with a little shorthand:
* `l[0:3]` - give me elements starting at index 0 and up to but not including index 3
* or more simply `l[:3]`
* negative indeces can be used to get items at the end