"""Week 14 - Activity 1: Registering decorated objects to an API."""

# This import gave Python 2 the Python 3 print() function. It is optional in Python 3.
from __future__ import print_function


# Stores each decorated function or class by name.
registry = {}


def register(obj):
    """Add a function or class to the registry and return it unchanged."""
    registry[obj.__name__] = obj
    return obj


@register
def spam(x):
    """Return x squared."""
    return x ** 2


@register
def ham(x):
    """Return x cubed."""
    return x ** 3


@register
class Eggs:
    """Store the fourth power of a supplied value."""

    def __init__(self, x):
        self.data = x ** 4

    def __str__(self):
        return str(self.data)


print("Registry:")
for name in registry:
    print(name, "=>", registry[name], type(registry[name]))

print("\nManual calls:")
print(spam(2))
print(ham(2))
X = Eggs(2)
print(X)

print("\nRegistry calls:")
for name in registry:
    print(name, "=>", registry[name](2))
