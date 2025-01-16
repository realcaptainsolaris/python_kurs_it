"""
Das Thema dieser Datei ist Polymorphie in der objektorientierten
Programmierung (OOP) in Python.

- Polymorphie bedeutet, dass Objekte verschiedener Klassen auf dieselbe
  Weise behandelt werden können, da sie gemeinsame Methoden oder Attribute besitzen.
- Dies fördert Flexibilität und Wiederverwendbarkeit von Code.
- Polymorphie wird oft in Kombination mit Vererbung verwendet.
"""

# Beispiel 1: Polymorphie mit Vererbung


class Animal:
    """Basisklasse für Tiere."""

    def speak(self):
        """Allgemeine Methode, die von Kindklassen überschrieben wird."""
        return "Das Tier macht ein Geräusch."


# Funktion, die Polymorphie demonstriert


# Beispielaufrufe


# Beispiel 2: Polymorphie mit gemeinsamen Schnittstellen


class Shape:
    """Basisklasse für verschiedene Formen."""

    def area(self):
        """Berechnet die Fläche der Form. Muss von den Kindklassen implementiert werden."""
        raise NotImplementedError(
            "Diese Methode muss in der Kindklasse überschrieben werden."
        )


# Liste von Formen


def print_areas(shapes):
    """Akzeptiert eine Liste von Shape-Objekten und gibt ihre Flächen aus."""


# Beispielaufrufe
shapes = []


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
