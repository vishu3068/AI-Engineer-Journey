# Day 9

## Exception Handling

### What is Exception?

Exception is an error that occurs during program execution.

Without exception handling the program crashes.

### Why use it?

- Prevents crashes
- Makes programs user-friendly
- Handles unexpected errors

## try

Used to write risky code.

```python
try:
    print(10/0)
```

## except

Handles the exception.

```python
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## else

Runs only if no exception occurs.

## finally

Runs always.

Used for cleaning resources like files and database connections.

## raise

Used to create custom exceptions.

```python
raise Exception("Invalid Age")
```

## Common Exceptions

- ZeroDivisionError
- ValueError
- TypeError
- IndexError
- KeyError
- NameError
- FileNotFoundError