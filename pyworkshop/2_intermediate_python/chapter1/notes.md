### Converting between types
* `str(value)` - stringify something.  Handles numbers, None.  Even collection types are stringified
```python
str(['hello', 'world']) # "['hello', 'world']"
str({ "key1": "value1", "key2": 35 }) # "{'key1': 'value1', 'key2': 35}"
```
* `int(value)` - only accepts numbers or strings that looks like integers
* `float(value)` - only accepts numbers or strings that looks like numbers

Python has `split` and `join` methods to explode or implode lists/strings.  
```python
'hello world'.split(' ') # ['hello', 'world']
' '.join(['hello', 'world']) # 'hello world'
```
Note that with `join`, the syntax is `delimiter_string.join(list)`