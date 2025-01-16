"""
Einführung in den Datentyp Dictionary in Python

Ein Dictionary (oder kurz `dict`) ist eine Sammlung von Schlüssel-Wert-Paaren.
Jeder Schlüssel (Key) ist eindeutig und dient als Index, um einen Wert (Value)
zu speichern und abzurufen. Dictionaries sind veränderlich, d. h.,
Schlüssel-Wert-Paare können hinzugefügt, geändert oder entfernt werden.

Themenübersicht:
1. Erstellung und Initialisierung von Dictionaries
2. Zugriff auf Werte und Schlüssel
3. Hinzufügen, Ändern und Entfernen von Einträgen
4. Iteration über Dictionaries
5. Wichtige Methoden
"""
students = ["Bob", "Alice"]
grades = [1, 2]

for index, student in enumerate(students):
    print(f"{student} hat die Note {grades[index]}")

# 1. Erstellung und Initialisierung von Dictionaries
# Ein Dictionary wird mit geschweiften Klammern `{}` erstellt.

# kEY:VALUE
students = {
    "Bob": 1,
    "Alice": 2,
}

# Ideal zum Umwandeln in einen Dataframe (mit Pandas)
student_table = {
    "names": ["Bob", "Alice"],
    "grades": [1, 2]
}

# print(students["1"]) # KeyError: 1

# 2. Zugriff auf Werte und Schlüssel
# Zugriff auf einen Wert über den Schlüssel
print(students["Bob"])

# Verwenden der Methode `get()`, um einen Wert abzurufen
# Vorteil: Verursacht keinen Fehler, wenn der Schlüssel nicht existiert
print(students.get("Grumpy", "nicht vorhanden"))
# students["Grumpy"] # KeyError
# students[0]  # KeyError

# 3. Hinzufügen, Ändern und Entfernen von Einträgen
# Hinzufügen eines neuen Eintrags
students["Mallory"] = 3

# Ändern eines vorhandenen Eintrags
students["Bob"] = 4

# Entfernen eines Eintrags mit `del`
# del students["Mallory"]

# Entfernen und Rückgabe eines Werts mit `pop()`

# 4. Iteration über Dictionaries
# Iteration über Schlüssel
for key in students:
    print(key)

# Iteration über Werte
for value in students.values(): # [4, 2, 3]
    print(value)

# Iteration über Schlüssel-Wert-Paare
for key, value in students.items(): # [("Bob", 4), ("Alice", 2), ...)]
    print(key, value)

# 5. Wichtige Methoden
# `keys()`: Gibt eine Ansicht aller Schlüssel zurück

# `values()`: Gibt eine Ansicht aller Werte zurück

# `items()`: Gibt eine Ansicht aller Schlüssel-Wert-Paare zurück

# Aufgabe: Schreiben Sie ein Programm, das ein Dictionary von Studenten
# erstellt. Jeder Schlüssel soll eine Matrikelnummer und jeder Wert ein Name
# sein. Implementieren Sie:
# 1. Hinzufügen neuer Studenten
# 2. Abrufen eines Studenten anhand der Matrikelnummer
# 3. Entfernen eines Studenten
# 4. Iteration über alle Studenten, um Name und Matrikelnummer auszugeben.
