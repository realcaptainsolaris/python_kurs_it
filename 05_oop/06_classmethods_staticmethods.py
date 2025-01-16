"""
Das Thema dieser Datei ist die Verwendung von `@classmethod` und
`@staticmethod` in der objektorientierten Programmierung (OOP) in Python.

- `@classmethod` ist eine Methode, die Zugriff auf die Klasse, aber nicht
  auf Instanzattribute hat. Sie wird mit dem ersten Parameter `cls` definiert.
- `@staticmethod` ist eine Methode, die weder Zugriff auf die Klasse noch auf
  Instanzattribute hat. Sie funktioniert wie eine normale Funktion innerhalb
  einer Klasse.
"""

# Beispiel 1: Verwendung von @classmethod


class MyClass:
    """Eine Beispielklasse mit einer Klassenmethode."""

    counter = 0  # Klassenattribut


# Beispielaufrufe der Klasse MyClass

# Aufgabe:
# Füge ein weiteres Klassenattribut hinzu, z. B. `name`, und eine
# Klassenmethode, die dieses Attribut zurückgibt oder setzt.

# Beispiel 2: Verwendung von @staticmethod


# Beispielaufrufe der statischen Methoden

# Aufgabe:
# Füge weitere statische Methoden hinzu, z. B. für Subtraktion oder Division.


# Beispiel: Factory-Methode mit @classmethod


class Fahrzeug:
    pass


# Beispiel 4: Unterschiede zwischen @classmethod und @staticmethod


class Example:
    """Eine Klasse, die den Unterschied zwischen classmethod und staticmethod zeigt."""

    pass


# Beispielaufrufe der Klasse Example
