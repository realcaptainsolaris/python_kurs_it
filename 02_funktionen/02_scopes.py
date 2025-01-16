"""
Funktionen und Scopes in Python

Der Scope (Gültigkeitsbereich) bestimmt, wo Variablen definiert und verwendet
werden können. Python unterscheidet zwischen lokalem, globalem und
nicht-lokalem Scope. Das Verständnis von Scopes ist wichtig, um Funktionen
effektiv zu nutzen und Fehler durch unerwartete Variablenänderungen zu
vermeiden.

Themenübersicht:
1. Lokaler Scope
2. Globaler Scope
3. Die `global`-Anweisung
"""
THRESHOLD = 2
x = 1 # x liegt im globalen Scope
id_ = "asdfjkdsa" # um nicht die Funktion id() zu überschreiben
counter = 0

# 1. Lokaler Scope
# Variablen, die innerhalb einer Funktion definiert werden, sind lokal
# und außerhalb der Funktion nicht sichtbar.
def fn():
    """Zeige Verhalten von lokaler Variable."""
    local_var = 1
    # print("x:", x)
    # sum = 3 # würde Funktion sum() überschreiben
    x = 2
    print(sum([1, 2, 3]))

fn()
print("x aus global:", x)

# print(local_var)  # Fehler: local_var ist außerhalb nicht definiert

# 2. Globaler Scope
# Variablen, die außerhalb von Funktionen definiert werden, sind global
# und können überall im Code verwendet werden.
def g():
    print(f"{THRESHOLD=}")

g()

# 3. Die `global`-Anweisung
# Mit der `global`-Anweisung kann innerhalb einer Funktion eine globale
# Variable verändert werden.

def alt_increment_counter():
   zz = zz + 1 # Unbound local error
   # x = counter + 1

# alt_increment_counter()

def increment_counter():
   # bad practice, global zu benutzen
   global counter
   global blablubb
   blablubb = 42
   counter += 1

increment_counter()
increment_counter()
increment_counter()
print(f"{counter=}")
print(f"{blablubb=}")

# Seiteneffekte: Funktionen ändern übergebenen veränderbaren Wert, zb. Liste, Dict, ...

def change_list(values):
    """hängt Werte an Values an."""
    values_neu = values.copy()
    values_neu.append(3)
    return values_neu


werte = [1, 42, 73]
werte_neu = change_list(werte)

print(f"{werte=}")
print(f"{werte_neu=}")


