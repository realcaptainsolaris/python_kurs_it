"""
Einführung in Funktionen in Python

Funktionen sind ein zentrales Konzept in Python, das es ermöglicht, Code
wiederverwendbar und modular zu gestalten. Mit Funktionen können Aufgaben
kapsuliert, Parameter verarbeitet und Ergebnisse zurückgegeben werden.

Themenübersicht:
1. Definition und Aufruf von Funktionen
2. Parameter und Argumente
3. Rückgabewerte
4. Standardwerte und Keyword-Argumente
5. Dokumentation und Best Practices
"""

# 1. Definition und Aufruf von Funktionen
# Eine Funktion wird mit dem Schlüsselwort `def` definiert.

def greet():
    print("Hello Welt")


# Aufruf der Funktion
greet()


# 2. Parameter und Argumente
# Funktionen können Parameter akzeptieren, um Eingabewerte zu verarbeiten.
def fn(x):
    print(x)


# Aufruf mit einem Argument
fn(3)

# 3. Rückgabewerte
# Eine Funktion kann mit `return` einen Wert zurückgeben.
def summe(a, b):
    ergebnis = a + b
    return ergebnis

# Rückgabewert verwenden
result = summe(3, 54)
print("Result von Summe:", result)

x, y = divmod(23, 12)

# 4. Standardwerte und Keyword-Argumente
# Funktionen können Standardwerte für Parameter definieren.


# Aufrufe mit und ohne Standardwerte

# 5. Dokumentation und Best Practices
# Funktionen sollten mit einem Docstring dokumentiert werden, der ihre
# Aufgabe, Parameter und Rückgabewerte beschreibt.


def multiply(a, b):
    """Multipliziert zwei Zahlen.
    
    Args:
        a: (int or float): Operand a
        b: (int or float): Operand b
    
    Returns:
        (int oder float) Produkt von a und b

    """
    return a * b


multiply(3, 2)

# print(multiply.__doc__)
# Zugriff auf den Doc-String: multiply.__doc__

# Aufgabe: Schreiben Sie eine Funktion, die folgende Anforderungen erfüllt:
# 1. Einen Namen und ein Alter akzeptiert und eine Begrüßung ausgibt.
# "hallo Peter, du bist 28 Jahre alt"

# 2. Eine Funktion, die den Durchschnitt einer Liste von Zahlen berechnet.
# "Der Durchschnitt von [1, 2, 3, 4, 5] ist 3.0"
# sum([1, 2, 4])

# 3. Dokumentieren Sie die Funktionen mit einem Docstring.

def average(values):
    return sum(values) / len(values)

values = [1, 2, 3, 4, 5]
print(f"Der Durschnitt ist {average(values)}")

""" 
Erstelle eine Funktion check_values, die eine Liste mit float-Werten und einen
tupel übergeben bekommt. Die Funktion prüft, ob alle Elemente
im geschlossenen Interval [a, b] liegen. Der Rückgabewert ist ein boolean.
Erinnerung: geschlossenes Intervall bedeutet, dass das Intervall alle Werte inklusive der
Grenzwerte zwischen zwei bestimmten Zahlen einschließt

def check_values(values, interval):
    ...

values = [2, 2.2, 4, 2.3, 0.1]
interval = (1, 5.3)
result = check_values(values, interval)
Result: False  # Nicht alle Werte von values liegen im Interval [1, 5.3]

"""
def check_values(values, interval):
    a, b = interval  # Entpacken des tupels in a, b
    for value in values:
        if value < a or value > b:
            return False
    return True


values = [2, 2.2, 4, 2.3, 1.1]
interval = (1, 5.3)
result = check_values(values, interval)
print(result)