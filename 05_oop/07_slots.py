"""
Das Thema dieser Datei ist die Verwendung von `__slots__` in Python.

- `__slots__` wird verwendet, um den Speicherverbrauch von Objekten zu
  reduzieren, indem es die erlaubten Attribute einer Klasse einschränkt.
- Es verhindert die dynamische Erstellung neuer Attribute
  (außerhalb der definierten Slots).
- Dies ist besonders nützlich in speicherkritischen Anwendungen.
"""

# Beispiel 1: Verwendung von `__slots__`
import sys
# from pympler import asizeof  # pip install pympler


class Person:
    """Eine Klasse, die `__slots__` verwendet, um erlaubte Attribute festzulegen."""

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Beispielaufrufe der Klasse Person

# Versuch, ein nicht erlaubtes Attribut hinzuzufügen


# Beispiel 2: Speicheroptimierung durch `__slots__`


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class SlotPoint:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


# Beispiel 3: Einschränkungen von `__slots__`


class Animal:
    """Eine Basisklasse mit `__slots__`."""

    __slots__ = ["species"]


class Dog(Animal):
    """Eine abgeleitete Klasse ohne eigene `__slots__`."""

    pass


# Beispielaufrufe der Klasse Dog
dog = Dog()

# Beispiel 4: Verwendung von `__slots__` mit Properties


class Car:
    """Eine Klasse, die `__slots__` und Properties kombiniert."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
