# Working with Files
## Exception handling
### File permissions
#### Examples of errors/exceptions
- `ValueError`
- `SyntaxError`
- `OutOfBounds`
- `KeyError`
- `AttributeError`
- `ZeroDivisionError`

#### File permissions
- `r` - This is the default mode. It opens file for reading
- `w` - This mode opens file for writing. If file doesn’t exist, it creates a new file for us
- `x` - Creates a new file, if already exists then the operation fails
- `a` - Opens the file in append mode, if file doesn’t exist it, it creates a new one
- `t` - This is the default mode to open in text mode
- `b` - This is for binary mode
- `+` - This will open a file for reading and writing

**We have `try`, `except` and `finally`**
- `try` - Works as `if condition`
- `except` - Works as `elif`
- `finally` - Works as `else`, `finally` will execute regardless of `try` and `except` conditions

## `files_and_exception_handling.py`
```python
print(1/0)
```
Will give `ZeroDivisionError`
```python
num = 9
if num > 8
    print(num)
```
Will produce `SyntaxError` because we forgot the `:`

We will create a file with required permission and see what errors/exception are possible to be seen

First iteration
```python
file = open("order.txt") # open() takes a string arg with file name
print(file)
```
This will produce a `FileNotFoundError` since `order.txt` does not exist!

But let's make this more sophisticated:

Second iteration
```python
try:
    file = open("order.txt")
    print("File found") # `try` block required except or will throw and error
except FileNotFoundError as errmsg: # creating alias same as nick name
    print(f"File not found: {errmsg}")
finally: # `finally` will execute regardless of `try` and `except` block execution, also used to clean up code
    print("Thank you for visiting! See you again!")
```
It will try to open the file, and if it can't it prints a more personalised message out to the screen:
```commandline
File not found: [Errno 2] No such file or directory: 'order.txt'
Thank you for visiting! See you again!
```