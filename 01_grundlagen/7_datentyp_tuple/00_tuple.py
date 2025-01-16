"""
Einführung in den Datentyp `tuple` in Python

Ein Tuple (oder Tupel) ist eine geordnete, unveränderliche Sammlung von Elementen.
Im Gegensatz zu Listen können die Werte eines Tuples nach der Erstellung
nicht geändert werden. Tuples eignen sich gut für Daten, die unveränderlich
bleiben sollen.

Themenübersicht:
1. Erstellung und Eigenschaften von Tuples
2. Zugriff und Entpacken von Tuples
3. Verwendung von Tuples in Funktionen
4. Methoden und Anwendungen
"""

# 1. Erstellung und Eigenschaften von Tuples
# Tuples werden mit runden Klammern `()` erstellt.
names = ("Bob", "Alice")

# Leeres Tuple erstellen
leerer_tuple = ()

# Ein einzelnes Element benötigt ein Komma
tuple_ein_element = (1,)
print(type(tuple_ein_element))

falscher_tuple = (1) # !!!! das ist kein tupel, sondern int mit klammern
print(type(falscher_tuple)) # <class 'int'>

# Ohne Klammern (Tuple Packing)

# 2. Zugriff und Entpacken von Tuples
# Zugriff auf Elemente erfolgt über Indizes
names[0]

# Tuples sind unveränderlich
# fruits[0] = "orange"  # Dies würde einen Fehler verursachen

# Entpacken von Tuples klassisch
name_1 = names[0]
name_2 = names[1]

# Entpacken in Python (links genauso viele Varialben wie rechts Elemente des Tuples)
name_1, name_2, name_3 = ("Bob", "Alice", "Grumpy")



# 3. Verwendung von Tuples in Funktionen
# Funktionen können mehrere Werte als Tuple zurückgeben
def fn(a, b):
    return a**2, b**2, 234


a, b, c = fn(4, 5)
print(a, b, c)

# 4. Methoden und Anwendungen
# `count()`: Zählt, wie oft ein Element im Tuple vorkommt

# `index()`: Gibt den Index des ersten Vorkommens eines Elements zurück

# Anwendung: Tuples als Schlüssel in Dictionaries
coord = (0,0)
d = {
    coord: 343
}

print(d[coord])


# Viele Funktionen / Methoden erzeugen einen Tupel
x, y = divmod(30, 2)