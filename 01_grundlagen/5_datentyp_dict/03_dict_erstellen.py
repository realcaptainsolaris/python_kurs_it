"""
Erstellen von Dictionaries in Python

Dictionaries können auf verschiedene Arten erstellt werden. Python bietet
flexible Möglichkeiten wie Literale, den `dict`-Konstruktor oder die Verwendung
von `zip`, um Schlüssel-Wert-Paare zu definieren.

Themenübersicht:
1. Erstellung mit Literalen
2. Erstellung mit dem `dict`-Konstruktor
3. Erstellung mit `zip`
"""

# Keys müssen immer unveränderliche Datentypen sein
# d[[1, 2]] = "asd" # TypeError: unhashable type: 'list'


# 1. Erstellung mit Literalen
# Ein Dictionary kann direkt mit geschweiften Klammern erstellt werden.

# Leeres Dictionary erstellen
d = {}
d["name"] = ["Tom", "Sawyer"]


# 2. Erstellung mit dem `dict`-Konstruktor
# Der `dict`-Konstruktor kann verwendet werden, um ein Dictionary aus
# Schlüssel-Wert-Paaren zu erstellen.
bands = dict(metal="Metallcia", pop="Prince")
print(bands)


# Erstellung aus einer Liste von 2er-Tupeln/Listen
de_en = [
    ["katze", "cat"],
    ["Hund", "dog"]
]
de_en_dict = dict(de_en)
print(de_en_dict)

# 3. zip

students = ["Bob", "Alice"]
grades = [1, 2]
ages = [24, 22]

zippo = zip(students, grades, ages)
name, note, alter = next(zippo)
print(name, note, alter)

# so ähnlich macht das zip im Hintergrund
for name, grade, age in [('Bob', 1, 24), ('Alice', 1, 24)]:
    print(name, grade, age)

# zip erzeugt pro Iteration jeweils ('Bob', 1, 24)
for name, grade, age in zip(students, grades, ages):
    print(name, grade, age)


# 4. Dict mit zip erstellen
# `zip` kann verwendet werden, um zwei Sequenzen zu einem Dictionary zu kombinieren.

students = ["Bob", "Alice"]
grades = [1, 2]

student_dict = dict(zip(students, grades))
print(student_dict)