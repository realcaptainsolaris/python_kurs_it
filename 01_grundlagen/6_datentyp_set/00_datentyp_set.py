"""
Einführung in den Datentyp `set` in Python

Ein Set (Menge) ist eine ungeordnete Sammlung von einzigartigen Elementen.
In Python wird der Datentyp `set` verwendet, um Mengen zu repräsentieren.
Er eignet sich besonders für Operationen wie Vereinigung, Schnittmenge oder
Unterschied.

Themenübersicht:
1. Erstellung und Eigenschaften von Sets
2. Hinzufügen und Entfernen von Elementen
3. Mengenoperationen: Vereinigung, Schnittmenge, Unterschied
4. Methoden und Anwendungen
"""

s = {1, 2}
print(bool(s))

s = set()
print(bool(s))

# 1. Erstellung und Eigenschaften von Sets
# Ein Set wird mit geschweiften Klammern `{}` oder der Funktion `set()` erstellt.
# Sets enthalten keine doppelten Elemente.
namen = ["Bob", "Bob", "Alice", "Alice", "Grumpy"]
namen_unique = []
for name in namen:
    if name not in namen_unique:
        namen_unique.append(name)


namen = list(set(namen))
print("Eindeutige Liste:", namen)

# Erstellung eines leeren Sets (Achtung: {} erzeugt ein leeres Dictionary)

# Automatische Entfernung doppelter Elemente

# 2. Hinzufügen und Entfernen von Elementen
# `add()`: Fügt ein Element hinzu.

# `remove()`: Entfernt ein Element (KeyError, wenn das Element nicht existiert).

# `discard()`: Entfernt ein Element (kein Fehler, wenn das Element nicht existiert).

# `pop()`: Entfernt ein zufälliges Element.

# `clear()`: Entfernt alle Elemente aus dem Set.

# 3. Mengenoperationen
set_c = {1, 2}
set_d = {3, 4}
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Vereinigung (`union()` oder `|`)
print(set_a | set_b)

# Schnittmenge (`intersection()` oder `&`)
print(set_a & set_b)

# Unterschied (`difference()` oder `-`)
print(set_a - set_b)

# Symmetrische Differenz (`symmetric_difference()` oder `^`)
print(set_a ^ set_b)

# 4. Methoden und Anwendungen
# `issubset()`: Prüft, ob ein Set eine Teilmenge eines anderen ist.
print(set_c < set_a)

# `issuperset()`: Prüft, ob ein Set eine Obermenge eines anderen ist.
print(set_a > set_c)

# `isdisjoint()`: Prüft, ob zwei Sets keine gemeinsamen Elemente haben.

list_a = [1, 2]
list_b = [3, 4]

print(set(list_a).isdisjoint(set(list_b)))