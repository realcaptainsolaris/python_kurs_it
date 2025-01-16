"""
Das Thema dieser Datei ist eine Einführung in das Exception Handling in Python.

- Exceptions treten auf, wenn im Programm ein Fehler auftritt.
- Mit Exception Handling können Fehler abgefangen und behandelt werden,
  ohne dass das Programm abstürzt.
- Die wichtigsten Keywords sind `try`, `except`, `else` und `finally`.
"""

# Beispiel 1: Grundlagen des Exception Handling

user_input = int("0")

try:
    a = 3
    z = 3 / user_input
except:
    print("a:", a)
    print("Division durch 0 hat nicht geklappt")


# Rechne Userinput um in Float
user_input = "3.2"
try:
    f = float(user_input)
except:
    print("umwandlung fehlgeschlagen")



def divide(a, b):
    """Teilt zwei Zahlen und behandelt Division durch Null."""
    return a / b 


# Beispielaufrufe der Funktion
print(divide(10, 2))  # 5.0
try:
    # print(divide(10, 0))  # Zero Division Fehler
    print(divide(10, "10")) 
except ZeroDivisionError as e:
    print("Es ist folgender Fehler aufgetreten:", e)
except TypeError as e:
    print("Es ist ein TypeError aufgetreten:", e)


# Aufgabe: schreibe eine Funktion is_float(value), 
# die True zurück gibt, falls value zu float castbar ist
# die False zurück gibt, falls Nein


# Beispiel 3: Nutzung von `else` und `finally`


def read_file(file_path):
    """Liest eine Datei ein und behandelt mögliche Fehler."""
    pass


# Fehler in einem Block gruppieren
try:
    zahl1 = int(input("Gib die erste Zahl ein: "))
    zahl2 = int(input("Gib die zweite Zahl ein: "))
    
    ergebnis = zahl1 + zahl2
    print(f"Das Ergebnis der Addition ist: {ergebnis}")
except (ValueError, TypeError) as e:
    print(f"Fehler erkannt: {e}")
finally:
    print("Berechnung abgeschlossen.")

