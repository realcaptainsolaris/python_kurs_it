"""
Einführung in den Datentyp Liste in Python

Listen sind eine grundlegende Datenstruktur in Python. Sie erlauben das
Speichern und Verarbeiten von mehreren Elementen in einer geordneten Sequenz.
Listen sind veränderlich, d. h., ihre Elemente können nach der Erstellung
geändert werden.

Themenübersicht:
1. Erstellung und Initialisierung von Listen
2. Wichtige Operationen und Methoden
3. Vergleich von Listen
4. Überprüfung von Listeninhalten
5. Prüfung auf Leere und Existenz
"""

# 1. Erstellung und Initialisierung von Listen
fruits = ["banana", "apple", "quince"]
fruits2 = ["apple"]

print(type(fruits)) # class list

# 2. Wichtige Operationen und Methoden
# Operatoren können verwendet werden, um Listeninhalte zu prüfen oder Listen
# zu vergleichen.

# Überprüfung, ob ein Element in einer Liste vorhanden ist
if "apple" in fruits:
    print("apple ist in der liste")  # "apple" == "apple"

# in Operator auf Strings
text = "apples are good for us"
if "apple" in text:
    print("das ist wahr")


# Länge einer Liste
print(len(fruits)) 

# 3. Vergleich von Listen
# Listen werden auf Elemente und Reihenfolge geprüft.
a = [1, 2, 3]
b = [1, 2, 3]
if a == b:
    print("listen sind gleich")

# Reihenfolge ist entscheidend
if a == [1, 3, 2]:
    print("listen sind gleich") # das trifft im Beispiel aber nicht zu!
else:
    print("listen sind NICHT gleich")

# Identität von Listenobjekten

# 4. Überprüfung von Listeninhalten
# Methoden und Bedingungen, um den Inhalt von Listen zu überprüfen.

# Schlechte Praxis: Prüfen, ob mindestens ein Element in der Liste ist
if len(fruits) > 0:
    print("es beinfdet sich min ein Element in der Liste")

# Gute Praxis: Prüfen, ob Liste nicht leer ist
if fruits:
    print("Pythonisch abgefragt, ob die Liste min. ein Element hat.")

# Überprüfung, ob eine Liste leer ist
example = []
if not example:
    print("die liste example ist leer")

# Auch noch überprüfen, ob es eine Liste ist
if isinstance(example, list) and not example:
    print("es ist definitiv eine liste example ist leer")


