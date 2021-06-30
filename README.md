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