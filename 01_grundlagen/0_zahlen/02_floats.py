"""
Fließkommazahlen in Python: Stellen, Präzision und Probleme

Fließkommazahlen werden in Python mit dem Typ `float` dargestellt. Dieser
ermöglicht die Darstellung von Dezimalzahlen und unterstützt auch die
wissenschaftliche Notation. Allerdings gibt es wichtige Aspekte und
Einschränkungen, die beachtet werden sollten.
Er enstpricht dem C Datentyp double (64 bit), und ist in IEEE 754 spezifiziert.

Themenübersicht:
1. Eigenschaften von Fließkommazahlen
2. Probleme mit der Präzision
3. Rundung und Formatierung
4. Wissenschaftliche Notation
5. Typkonvertierungen: int, float, str
"""
import math


# 1. Eigenschaften von Fließkommazahlen
# Fließkommazahlen werden mit einer begrenzten Präzision gespeichert.
x = 0.1
print(x, type(x)) # <class 'float'>

# 2. Probleme mit der Präzision
# Manche Zahlen können nicht exakt als Binärwerte dargestellt werden.
# Beispiel für ein Problem der Präzision:
x = 0.1 + 0.1 + 0.1   #  0.30000000000000004

# 3. Rundung und Formatierung
# Python bietet Funktionen, um Fließkommazahlen zu runden oder zu
# formatieren.
# Beispiel: Runden auf zwei Dezimalstellen
x = 1.4323
print("Round:", round(x, 2))  # 1.43

# Bankers' Rounding
# Python verwendet standardmäßig "Bankers' Rounding" in der Funktion
# `round()`. Dabei werden Werte genau zwischen zwei Zahlen (z. B. 2.5)
# zur nächsten geraden Zahl gerundet.
# zum kaufmännisches 
print("Runde 2.5 auf: ", round(2.5))  # 2 nächste gerade Int ist 2
print("Runde 3.5 auf: ", round(3.5))  # 4 nächste gerade Int ist 4
print("Runde 4.5 auf: ", round(4.5))  # 4 nächste gerade Int ist 4

# 4. Wissenschaftliche Notation
# Fließkommazahlen können in der wissenschaftlichen Notation dargestellt
# werden.
large_number = 5.6e5 # 5.6 * 10 ^ 5
print(3 / 1000**3)  # wird in wissenschaflticher Notation dargestellt: 3e-09

# 5. Typkonvertierungen: int, float, str
# Umwandlung von int zu float
print(float(42))

# Umwandlung von float zu int
# Dabei werden Nachkommastellen abgeschnitten (nicht gerundet).
print(int(42.34))

# Umwandlung von str zu float
# Nur gültig, wenn der String eine gültige Fließkommazahl enthält.
print(float("42.23"))
print(float("-inf"))  # nan, inf, -inf

# Fehlerfall bei ungültiger Konvertierung
# float("a3")


# Ab- und Afrunden zum nächsten Integer
x = 34.643
print(math.floor(x)) # Abrunden (untere Gaussklammer)
print(math.ceil(x)) # Aufrunden 

print(math.floor(-3.24))  # -4
x = math.trunc(-3.24)  # Ergebnis Int
print(x, type(x))  # -3 /trunc schneidet Nachkommateil ab

