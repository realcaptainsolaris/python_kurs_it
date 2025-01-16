"""
Python Integer und arithmetische Operatoren

In Python werden Ganzzahlen als Integer bezeichnet und durch den Datentyp
`int` repräsentiert. Arithmetische Operatoren erlauben mathematische
Berechnungen wie Addition, Subtraktion, Multiplikation und Division.
Hierbei sind auch fortgeschrittene Operatoren wie Modulo oder
Exponentialrechnung verfügbar.

Besonderheiten:
- Integer in Python haben keine feste Größenbeschränkung, sondern nur
  eine Speichergrenze durch die verfügbare Hardware.
- Division mit `/` erzeugt immer einen Fließkommawert (float), selbst
  wenn das Ergebnis mathematisch eine Ganzzahl ist.

Beispiele für arithmetische Operatoren:
- Addition: `+`
- Subtraktion: `-`
- Multiplikation: `*`
- Division: `/`
- Ganzzahlige Division: `//`
- Modulo: `%`
- Potenzierung: `**`

Weitere nützliche builtin Funktionen:
- `sum()`: Summiert alle Werte in einer Sequenz.
- `min()`: Gibt den kleinsten Wert einer Sequenz zurück.
- `max()`: Gibt den größten Wert einer Sequenz zurück.

https://docs.python.org/3/reference/expressions.html#operator-precedence
"""

# Initialisierung von Variablen
# Ganzzahlen werden direkt durch Zuweisung initialisiert
x = 12

# Den Typ einer Variablen überprüfen
print("Der Datentyp von x:", type(x)) # <class 'int'>

# große Zahlen können mit _ getrennt werden
population = 10_000_000

# Konstanten gibt es in Python nur als Konvention
# Sie werden großgeschrieben und sollten nicht verändert werden
THRESHOLD = 12

# Addition: Zwei Ganzzahlen addieren
# Hier werden zwei Zahlen addiert und das Ergebnis ausgegeben
y = 34
z = x + y

# Subtraktion: Zwei Ganzzahlen subtrahieren
# Hier wird die zweite Zahl von der ersten abgezogen

# Multiplikation: Zwei Ganzzahlen multiplizieren
# Das Ergebnis der Multiplikation wird hier berechnet

# Division: Eine Ganzzahl durch eine andere teilen
# Division liefert ein Ergebnis als Fließkommazahl
result = 4 / 2  # Ergebnis von Division ist Float
print("Result:", result, type(result))

# Ganzzahlige Division: Nur den ganzzahligen Anteil der Division ausgeben
# Das Ergebnis ist eine Ganzzahl (Abrunden zum nächsten kleineren Wert)
result = 4 // 2
print("Result von Floordiv:", result)

# Modulo: Den Rest einer Division berechnen
# Das Ergebnis ist der Rest der Division von x durch y
result = 5 % 2 
print("Result von Modulo:", result)

# Potenzierung: Eine Zahl mit der Potenz einer anderen Zahl berechnen
# Hier wird x hoch y berechnet
z = 3
result = z**2  # Potenz, 3 ^ 2

# Verwendung von min(), max()
print("Minimum:", min(1, 4, 0, -23))  # -23
print("Maximum:", max(1, 4, 0, -23))  # 4
print("Summe:", sum([1, 2, 54, 4]))  # 61


# Aufgabe
# Wieviele Baumstämme passen der Länge nach in die Halle?
# Baumstamm-Länge 4, Hallenlänge 19. Wieviele Meter sind noch übrig?
# Nutze Konstanten und Variablen.
HALL_LENGTH = 19
tree_length = 4
total_trees = HALL_LENGTH // tree_length
total_rest = HALL_LENGTH % tree_length
print("Es passen in die Halle: ", total_trees, "Baumstämme")
print("Es ist übrig: ", total_rest, " Meter")
print("divmod:", divmod(19, 4))


# Ein String kann als Integer konvertiert werden
zahlen_string = "3"
zahl = int(zahlen_string)