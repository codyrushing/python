## REPL
Can enter repl just by running `python`
* just like JS.  Useful built-in methods:

* `type(var)` - tells you what type `var` is.  Think `typeof`.
* `dir(var)` - tells you all of the methods that are available on `var`.  Sort of like printing an object's prototype.
* `help(type)` - eg `help(str)` prints some help info on methods on class `str`

Gotchas:

* variable can't start with a number
* python lets you overwrite built in types.  eg: `list = 'abc'`.  This overrites `list`, which is a built in method for making lists, So don't do that

### Strings
* can concatenate just like JS with `+` 
```python
"abc" + "123"
```
unlike JS, it will not coerce values of non-string type to strings.  so `"abc" + 123` will error since `123` is not a string

* multi-line-strings can be made with `"""` just like triple back tick
```python
long_string = """
hey
y'all
what's up
"""
```
`long_string` would be automatically constructed with new line characters at the line breaks.

* f strings for string interpolation
```
name = "Cody"
f"My name is {name}"
```

### Printing
`print()` is `console.log()`

# Parallelism
* As of Python 3.2, there is a [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) module for handling concurrency.  It has support both for threads and processes, which is cool.  [Here is an example of how to do it with simple requests](https://dev.to/rhymes/how-to-make-python-code-concurrent-with-3-lines-of-code-2fpe).