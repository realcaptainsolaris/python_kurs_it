"""
Datentyp String in Python

In Python repräsentiert der Datentyp `str` Zeichenketten (Strings). Strings
sind immutable, d. h., sie können nach ihrer Erstellung nicht verändert
werden. Python bietet zahlreiche Methoden zur Verarbeitung und Analyse
von Strings.

Themenübersicht:
1. Eigenschaften von Strings
2. Die Funktion `len`
3. Wichtige String-Methoden
   - Methoden zur Prüfung: `.isxxx()`
   - Suche innerhalb von Strings: `.index()`, `.find()`, `.rfind()`
4. Indexierung und Slicing
5. Konkatenierung und Maskierung
6. Zusätzliche String-Methoden
"""

# 1. Eigenschaften von Strings
# Strings können durch einfache oder doppelte Anführungszeichen erstellt werden.
name = "Bob"
username = 'Alice'
alter_ego = "Bob sagt 'hi'"
print(name, type(name))  # <class 'str'>

# 2. Die Funktion `len`
# `len` gibt die Länge eines Strings zurück, d. h., die Anzahl der Zeichen.
name = "Ärno"
print(len(name))

print(ord("Ä"))  # Unicode Codepoint anzeigen
print(chr(1276)) # Ӽ

# 3. Wichtige String-Methoden

# Methoden zur Prüfung: `.isxxx()`
# Beispiele für `.isxxx()`-Methoden:


# Suche innerhalb von Strings

# `.index()`: Gibt die Position des ersten Vorkommens zurück
# (löst einen Fehler aus, wenn das Zeichen nicht gefunden wird).
name = "Ärno"
print("Index von r:", name.index("r"))

# `.find()`: Gibt die Position des ersten Vorkommens zurück
# (gibt -1 zurück, wenn das Zeichen nicht gefunden wird).
print("Index von x:", name.find("x")) # -1

# `.rfind()`: Sucht von rechts und gibt die Position des letzten
# Vorkommens zurück.

# 4. Indexierung
# Strings können über ihre Indizes (Positionen) angesprochen werden.
print("Index-Operator:", name[0]) # Ä

# 5. Konkatenierung und Maskierung
# Strings können mit `+` verbunden (konkateniert) werden.
name = "Bob" + "Gans"
print("Bob + Gans:", name)

sternchen = "*" * 40  # erzeugt String von 40 Zeichen
print(sternchen)

# Maskierung von Sonderzeichen erfolgt mit einem Backslash (`\`).
print("hallo\nwelt\thierkommt der Tab")

# 6. Zusätzliche String-Methoden
string_methods_example = "  Python Programmierung \n "

# Entfernen von Leerzeichen oder spezifischen Zeichen
print(string_methods_example.strip())   # trim beidseitig
print(string_methods_example.rstrip())  # trim rechts
print(string_methods_example.lstrip())  # trim left

string = "**?hier ist der Wert***&%"
print(string.strip("*?&%"))  # Diese Zeichen werden vorne und hinten getrimmt

# Aufteilen in eine Liste
names = "Bob Alice Grumpy"
print(names.split())  # default Trenner ist Leerzeichen

# Ersetzen von Zeichen oder Teilstrings
print(names.replace("Bob", "Bobby"))

# Prüfen, ob ein String mit einer bestimmten Sequenz beginnt oder endet
print(names.startswith("Bo"))  # True
print(names.endswith("x"))  # False

# Änderung der Groß-/Kleinschreibung
string_methods_example = "bob bla blubb ß"
print("Erster Buchstabe groß:", string_methods_example.capitalize())
print("Jedes Wort groß:", string_methods_example.title())
print("Alles klein:", string_methods_example.lower())
print("Alles groß:", string_methods_example.upper())
print("Kleinschreibung (casefold):", string_methods_example.casefold())


# Zählen von Teilstrings
x = "a a aabba"
print("Vorkommen von a:", x.count("a"))


