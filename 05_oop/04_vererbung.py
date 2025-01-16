"""
Das Thema dieser Datei ist die Vererbung in der objektorientierten
Programmierung (OOP) in Python.

- Vererbung erlaubt es, Eigenschaften und Methoden einer Basisklasse
  (Elternklasse) auf abgeleitete Klassen (Kindklassen) zu übertragen.
- Sie fördert Wiederverwendung und Erweiterbarkeit von Code.
- Die Basisklasse wird mit `class ChildClass(ParentClass):` vererbt.
"""

# Beispiel 1: Grundlagen der Vererbung


class Animal:
    """Basisklasse, die allgemeine Eigenschaften von Tieren definiert."""

    pass


# Kindklasse, die von Animal erbt


# Kindklasse, die von Animal erbt


# Beispielaufrufe der Klassen

# Aufgabe:
# Füge eine weitere Kindklasse hinzu, z. B. Bird, und implementiere eine
# spezifische `speak`-Methode.

# Beispiel 2: Verwendung der Basisklasse mit `super()`


class Vehicle:
    """Basisklasse für Fahrzeuge."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def description(self):
        """Gibt eine Beschreibung des Fahrzeugs zurück."""
        return f"Fahrzeug: {self.brand} {self.model}"


# Kindklasse, die die Basisklasse erweitert


# Beispielaufruf der Klasse Car

# Beispiel 3: Typprüfung mit `isinstance` und `issubclass`
print(isinstance(dog, Animal))  # True
print(isinstance(dog, Dog))  # True
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))  # False
