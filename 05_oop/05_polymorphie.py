"""
Das Thema dieser Datei ist Polymorphie in der objektorientierten
Programmierung (OOP) in Python.

- Polymorphie bedeutet, dass Objekte verschiedener Klassen auf dieselbe
  Weise behandelt werden können, da sie gemeinsame Methoden oder Attribute besitzen.
- Dies fördert Flexibilität und Wiederverwendbarkeit von Code.
- Polymorphie wird oft in Kombination mit Vererbung verwendet.
"""

class Shape:
    """Basisklasse für verschiedene Formen."""

    def area(self):
        """Berechnet die Fläche der Form. Muss von den Kindklassen implementiert werden."""
        raise NotImplementedError(
            "Diese Methode muss in der Kindklasse überschrieben werden."
        )


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        from math import pi
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a 
        self.b = b 

    def area(self):
        return self.a * self.b


def print_areas(shapes):
    """Akzeptiert eine Liste von Shape-Objekten und gibt ihre Flächen aus."""
    for shape in shapes:
        print(shape.area())


# Beispielaufrufe
shapes = [
    Circle(3), Circle(92), Rectangle(2, 1), Circle(2), Rectangle(12, 1)
]
print_areas(shapes)


# Beispiel 3: Polymorphie mit benutzerdefinierten Funktionen


def describe(obj):
    """Gibt eine Beschreibung eines Objekts aus, basierend auf dessen Typ."""
    if hasattr(obj, "speak"):
        print(obj.speak())
    elif hasattr(obj, "area"):
        print(f"Fläche: {obj.area()}")
    else:
        print("Unbekanntes Objekt.")


# Beispielaufrufe
