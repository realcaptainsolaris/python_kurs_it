"""
Kontrollstrukturen: if, else und elif in Python

Die Kontrollstrukturen `if`, `else` und `elif` ermöglichen in Python
bedingte Anweisungen. Sie erlauben es, Code abhängig von bestimmten
Bedingungen auszuführen.

Themenübersicht:
1. Die if-Anweisung
2. Die else-Anweisung
3. Die elif-Anweisung
4. Verschachtelte Bedingungen
5. Kurzformen (Ternary Operator)
6. Die pass-Anweisung
"""

# 1. Die if-Anweisung
# Die if-Anweisung prüft eine Bedingung und führt den nachfolgenden Code aus,
# wenn die Bedingung True ergibt.
x = 10
if x >= 10:
    print("ja, x ist größergleich als 10")

if x <= 24:
    print("ja x ist kleiner als 24")
    print("huurah")
    
# 2. Die else-Anweisung
# Die else-Anweisung wird ausgeführt, wenn die if-Bedingung False ergibt.
if x < 3:
    print("x ist < 3")
else:
    print("x ist nicht kleiner als 3")


if x > 10 or len("grumpy") > 4:
    print("grumpy is true")


# 3. Die elif-Anweisung
# Mit elif können mehrere Bedingungen geprüft werden.
z = 7
if x > z:
    print("x > z")
elif z > 10:
    print("z > 10")
elif x != 10:
    print("x != 10")
else:
    print("ansonsten halt das")

# 6. Die pass-Anweisung
# Die pass-Anweisung wird verwendet, um eine leere Code-Struktur zu erstellen.
# Sie dient als Platzhalter, wenn kein Code ausgeführt werden soll.
value = 10
if value > 10:
    pass  # todo: email senden
else:
    pass  # todo: DB löschen
