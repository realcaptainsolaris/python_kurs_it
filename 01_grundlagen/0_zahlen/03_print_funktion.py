"""
Die print-Funktion in Python: Argumente, sep, end, flush

Die print-Funktion in Python bietet vielseitige Möglichkeiten, Ausgaben
im Terminal oder in der Konsole zu formatieren. Neben den Standard-
einstellungen für die Ausgabe können zusätzliche Parameter wie `sep` und
`end` verwendet werden, um die Ausgabe zu steuern.

Themenübersicht:
1. Mehrere Argumente
2. Der Parameter `sep`
3. Der Parameter `end`
"""

# 1. Mehrere Argumente
# Mit der print-Funktion können mehrere Argumente übergeben werden.
# Sie werden standardmäßig durch ein Leerzeichen getrennt.

# Ausgabe: Mehrere Argumente: 42 3.14 Text
print("42", 23, 3.2, [1, 2])

# 2. Der Parameter `sep`
# Der Parameter `sep` definiert das Trennzeichen zwischen den Argumenten.
print("Hallo", "Welt", "again", sep="-")

# 3. Der Parameter `end`
# Der Parameter `end` definiert das Zeichen, das am Ende der Ausgabe
# hinzugefügt wird. Standardmäßig ist dies ein Zeilenumbruch (\n).
print("hallo", end="\n\n")
print("welt")