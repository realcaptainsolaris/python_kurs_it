"""
Liste: Wichtige Methoden in Python

Listen sind eine der flexibelsten und am häufigsten verwendeten Datenstrukturen
in Python. Sie bieten eine Vielzahl von Methoden, um Elemente hinzuzufügen,
zu entfernen, zu suchen oder zu manipulieren.

Themenübersicht:
1. Hinzufügen von Elementen: `append()`, `extend()`, `insert()`
2. Entfernen von Elementen: `remove()`, `pop()`, `clear()`
3. Suchen und Zählen: `index()`, `count()`
4. Sortieren und Umkehren: `sort()`, `reverse()`
5. Kopieren von Listen: `copy()`
"""

# 1. Hinzufügen von Elementen
fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits 
fruits_real_copy = fruits.copy() # flache Kopie

print("Fruits:", id(fruits))
print("Fruits Copy:", id(fruits_copy))

if fruits is fruits_copy:
    print("Bei Fruits und Fruitscopy handelt es sich um das selbe Objekt")

x = None
if x is None:
    print("x ist None")

# Falsche Anwendung des Identitätsoperators is
# nicht für arithmetischen Vergleich nutzen.
y = 4
z = 4 
if y is z:
    print("y hat den gleichen wert wie z")  # ==


# `append()`: Fügt ein Element am Ende der Liste hinzu
fruits.append("birne")

# `extend()`: Fügt mehrere Elemente am Ende hinzu
fruits.extend(["melone", "icecream"])

# `insert()`: Fügt ein Element an einer bestimmten Position ein
fruits.insert(0, "quince")

# 2. Entfernen von Elementen
# `remove()`: Entfernt das erste Vorkommen eines Elements
fruits.remove("birne")

# `pop()`: Entfernt ein Element an einer bestimmten Position (Standard: letztes Element)
print(fruits)
print(fruits.pop())
print("fruits:", fruits)
print("fruit_copy:", fruits_copy)

# `clear()`: Entfernt alle Elemente aus der Liste
fruits.clear()

# 3. Suchen und Zählen
fruits = ["apple", "banana", "apple", "cherry"]

# `index()`: Gibt den Index des ersten Vorkommens eines Elements zurück

# `count()`: Zählt die Anzahl eines bestimmten Elements

# 4. Sortieren und Umkehren
numbers = [5, 2, 9, 1, 5, 6]

# `sort()`: Sortiert die Liste in aufsteigender Reihenfolge
numbers.sort()  # inplace Operation
print(numbers)

numbers_sorted = sorted(numbers, reverse=True) # sorted erzeugt neue liste! Reverse = dreht um
print(numbers_sorted)

# `reverse()`: Kehrt die Reihenfolge der Liste um
reversed_fruits = fruits[::-1]
print("Reversed:", reversed_fruits)

# 5. Kopieren von Listen
# `copy()`: Erstellt eine flache Kopie der Liste

# Änderung an der Kopie beeinflusst das Original nicht
