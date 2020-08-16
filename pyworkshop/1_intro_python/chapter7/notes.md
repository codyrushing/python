## `try` `except`
```python
try:
  int(a)
except Exception as e
  print(e)
```

Here is a simple try/except.  All built-in, non-system-exiting exceptions are derived from the `Exception` class. All user-defined exceptions should also be derived from `Exception`.  

You can also specify different exception classes to catch:

```python
try:
  # do something sketchy
except ValueError as e:
  print(e)
except IOError as (errno, strerror):
  print(strerror)
except Exception as e:
  print('something unknown happened', e);  
```

## Modules and imports

Python scripts know whether they are being run directly (ie. `python file.py`) as opposed to being imported by another python script.  There is a variable `__name__` which when a file is run directly is going to be `"main"`.  So you'll often see things like this in libs:

```python
if __name__ == 'main':
  # this block will not run when the file is being imported
```

#### Importing
```python
import some_lib # "some_lib" is either a third party library called "some_lib" or is a relative file lookup for "./some_lib.py"
```