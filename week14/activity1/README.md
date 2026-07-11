# Week 14 – Activity 1: Debugging Python Decorators

## Corrected code

The corrected and runnable program is in `activity1.py`. The supplied code needed line breaks restored and several special Python names corrected: `__future__`, `__name__`, `__init__`, and `__str__`.

## Line-by-line explanation

- `from __future__ import print_function` makes Python 2 use the Python 3 `print()` function. It is optional when running Python 3.
- `registry = {}` creates an empty dictionary that will hold decorated objects.
- `def register(obj):` defines a decorator that accepts a function or class.
- `registry[obj.__name__] = obj` stores the object under its name, such as `spam`, `ham`, or `Eggs`.
- `return obj` returns the original object unchanged, so the decorator registers it without intercepting later calls.
- `@register` immediately passes the following function or class to `register` after Python creates it.
- `def spam(x):` defines a function that returns `x ** 2`, the square of `x`.
- `def ham(x):` defines a function that returns `x ** 3`, the cube of `x`.
- `class Eggs:` defines a class and registers the class itself.
- `def __init__(self, x):` is the constructor called when an `Eggs` instance is created.
- `self.data = x ** 4` calculates the fourth power of `x` and stores it in the instance.
- `def __str__(self):` defines the text displayed when an `Eggs` instance is printed.
- `return str(self.data)` converts the stored number to a string.
- `print("Registry:")` prints a heading.
- `for name in registry:` visits the names of all registered objects.
- `print(name, "=>", registry[name], type(registry[name]))` prints each name, its object, and its type.
- `print("\nManual calls:")` starts the manual-call section; `\n` adds a new line.
- `print(spam(2))` calls the original `spam` function and prints `4`.
- `print(ham(2))` calls the original `ham` function and prints `8`.
- `X = Eggs(2)` creates an `Eggs` object whose `data` value is `16`.
- `print(X)` uses `Eggs.__str__()` and prints `16`.
- The final loop retrieves each callable from `registry` and calls it with `2`. Functions return numbers, while calling `Eggs` creates an instance that is displayed as `16`.

The decorator syntax:

```python
@register
def spam(x):
    return x ** 2
```

is equivalent to:

```python
def spam(x):
    return x ** 2

spam = register(spam)
```

## Decorator summary

A Python decorator is a callable that receives a function or class and returns an object that will be assigned to the original name. Decorators provide a reusable way to register objects or add behaviour without editing the main body of every function or class. Common uses include registration, logging, validation, access control, caching, and timing.

In this program, `register` is a registration decorator. It runs when each decorated definition is created, stores that object in `registry`, and returns the same object. Because it does not return a wrapper, later calls to `spam`, `ham`, and `Eggs` are not intercepted or changed.

## Possible modifications

The program could be extended to support custom registry names:

```python
def register_as(name):
    def decorator(obj):
        registry[name] = obj
        return obj
    return decorator


@register_as("square")
def spam(x):
    return x ** 2
```

If logging or validation is required, a function decorator could return a wrapper that performs extra work before or after calling the original function. `functools.wraps` should be applied to such a wrapper to retain the original function's name and documentation. Classes may need a separate decorator if their required behaviour differs from that of functions.

Other useful extensions include rejecting duplicate names, grouping registered objects into categories, removing entries, storing metadata, or validating that registered objects follow a required interface.

## Expected result

The manual and registry calls both produce `4`, `8`, and `16`. Function memory addresses in the registry display may differ on every run.

## Reference

Mark Lutz, *Learning Python*, 5th Edition, Chapter 39.
