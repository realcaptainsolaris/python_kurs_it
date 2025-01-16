"""
f-Strings und die Methode `format()` in Python

Python bietet leistungsfähige Möglichkeiten zur String-Formatierung. Zwei
häufig verwendete Ansätze sind f-Strings (seit Python 3.6) und die Methode
`format()`. Beide erlauben das Einfügen von Werten in Strings und das
Anpassen des Ausgabeformats.

Themenübersicht:
1. Grundlagen von f-Strings
2. Platzhalter und Formatierung mit `format()`
3. Darstellung von Zahlensystemen
4. Darstellung großer Zahlen mit Tausendertrenner
"""

# 1. Grundlagen von f-Strings
# f-Strings beginnen mit einem `f` oder `F` vor den Anführungszeichen.
# Innerhalb geschweifter Klammern `{}` können Variablen oder Ausdrücke
# direkt eingebettet werden.
name = "Alice"
age = 30

output = f"{name} hat gesagt sie ist {age} Jahre alt"
print(output)

# Sie können auch Ausdrücke oder Funktionen innerhalb der Klammern verwenden.
print(f"Das Ergebnis ist {min(2, -3, -45)}")

# Formatierung von Zahlen
pi = 3.14159265359
print(f"Pi gerundet: {pi:0.2f}")

# 2. Platzhalter und Formatierung mit `format()`
# Die Methode `format()` verwendet geschweifte Klammern `{}` als Platzhalter.
# Werte werden in der Reihenfolge der Argumente eingefügt.
output = "Der Name des Users ist {} und er ist {} Jahre alt"
print(output.format("Bob", 35))

mehrzeilige_string = """ 
der Name ist {}
das Alter ist {}
die Strasse {}
"""
print(mehrzeilige_string.format("Alice", 53, "Mühlweg"))


# Positionale Argumente können durch Indizes spezifiziert werden.
print("{1} und {0}".format("A", "B"))

# Benannte Argumente können ebenfalls verwendet werden.
print("{name} ist {age} Jahre alt.".format(name="David", age=25))

# 3. Darstellung von Zahlensystemen
# Zahlen können als Binär-, Oktal-, oder Hexadezimalwerte dargestellt werden.
print(f"{13:b}")  # 1101


# 4. Darstellung großer Zahlen mit Tausendertrenner
# Zahlen können mit einem Komma als Tausendertrenner formatiert werden.
large_number = 1234567890
print(f"Large Number {large_number:,}")  # 1,234,567,890

# Anpassung des Dezimaltrenners (z. B. für europäische Formate)
print(f"Large Number {large_number:_}")

# Deutsche Darstellung: 1.234.567.890
string = f"{large_number:_}".replace("_", ".") # 1_234_567_890
print(string)

# Beispiel: F-String vs. `format()`
height = 1.75
print(f"Meine Größe ist {height} Meter.")
print("Meine Größe ist {} Meter.".format(height))