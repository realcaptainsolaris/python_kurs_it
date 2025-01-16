"""
Das Thema dieser Datei ist das gezielte Auslösen von Exceptions mit `raise`
und das Erstellen eigener Exceptions in Python.

- Mit `raise` können gezielt Fehler ausgelöst werden.
- Benutzerdefinierte Exceptions ermöglichen die Definition spezifischer Fehler.
- Exceptions können genutzt werden, um Fehlverhalten im Code zu signalisieren
  und gezielt darauf zu reagieren.
"""
import math 
# Beispiel 1: Gezieltes Auslösen einer Exception


def ellipse_area(a: float, b: float) -> float:
    """Berechne die Ellipsenfläche."""
    if b > a:
        raise ValueError(
            "die kleine Halbachse darf nicht größer sein als die große Halbachse"
            )
    
    return a * b * math.pi


try:
    result = ellipse_area(a=15, b=132)
    print(f"{result=}")
except ValueError as e:
    print("Konnte nicht ausgerechnet werden:", e)








# Beispielaufrufe der Funktion


# Beispiel 2: Eigene Exception definieren


def validate_custom_age(age):
    """Prüft das Alter und verwendet eine benutzerdefinierte Exception."""
    pass


# Beispielaufrufe der Funktion

# Beispiel 3: Kombination von Exceptions


def process_input(value):
    """Verarbeitet eine Eingabe und behandelt spezifische Fehler."""
    pass


# Beispielaufrufe der Funktion
