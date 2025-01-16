"""
For-Schleifen in Python

Die for-Schleife ist eine der am häufigsten verwendeten Kontrollstrukturen
in Python. Sie wird verwendet, um über Sequenzen (wie Listen, Tupel oder Strings)
zu iterieren. Python bietet zusätzliche Funktionen wie `enumerate`, sowie
die Möglichkeit, Schleifen mit `break`, `continue` und `else` zu kontrollieren.

Themenübersicht:
1. Grundlagen der for-Schleife
2. Verwendung von `enumerate`
3. Steuerung der Schleife mit `break` und `continue`
4. Die `for-else`-Konstruktion
5. Filtern von Listen
"""

# 1. Grundlagen der for-Schleife
# Iteration über eine Liste
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Iteration über einen String (da String eine Sequenz ist)
word = "*#=%"
for c in word:
    print(c)

# Iteration über eine Range: 
# Pendant in C/C++/Java: for(int i = 0; i < 5; i += 2)
for i in range(0, 5, 2):
    print(i, end=" ")

print("i nach loop:", i)
print()

# 2. Verwendung von `enumerate`
# `enumerate` liefert den Index und das Element während der Iteration.

# klassisch
counter = 1
for fruit in fruits:
    print(counter, fruit)
    counter += 1  # counter++ in C

print("*" * 40)

# mit enumerate
for index, fruit in enumerate(fruits, start=1):  #[(1, "Cherry"), (2, "Birne")]
    print(index, fruit)

# Enumerate erzeugt einen Iterator, der Tupel aus Index und Wert zur Verfügung stellt
names = ["Bob", "Alice"]
enumerate_object = enumerate(names)  # enumerate-Objekt ist ein Iterator
# print(next(enumerate_object))
# print(next(enumerate_object))
# exit(1)



# 3. Steuerung der Schleife mit `break` und `continue`
# `break`: Beendet die Schleife vorzeitig.
for i in range(5): 
    if i > 3:
        break
    print(i, end="") 

print()
print("*" * 40)

# `continue`: Überspringt den aktuellen Schleifendurchlauf.
for i in range(5):  # [0, 1, 2, 3, 4]
    if i > 2:
        continue
    # hier aufwändige Berechnungen
    print(i, end="") 

print()
# 4. Die `for-else`-Konstruktion
# Der `else`-Block wird ausgeführt, wenn die Schleife nicht durch `break`
# beendet wird.

personen = ["Tom", "Peter", "Alf", "Grumpy"]  # Suche Person mit Gr
search = "X" # nach diesem Wort wird gesucht

# klassisch 
person_found = False
for person in personen:
    if person.startswith(search):
        print("Person gefunden")
        person_found = True
        break 

if not person_found:
    print(f"Person mit {search} nicht gefunden")

# pythonische Variante
for person in personen:
    if person.startswith(search):
        print("Person gefunden")
        break 
else:
    # wird ausgeführt, wenn for NICHT mit break abgegrochen wurde
    print(f"Person mit {search} nicht gefunden")



# 5. Filtern von Listen
# Eine Liste kann mit einer for-Schleife oder einer List Comprehension
# gefiltert werden.

# Beispiel: Filterung mit einer for-Schleife
numbers = [10, 12, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = []
for number in numbers:
    if number > 3 and number < 9:
        filtered_numbers.append(number)

print(filtered_numbers)


# Die Menge aller Tuple (i, i^2) klassisch
menge = []
for i in range(1, 5):
    menge.append( (i, i**2) )
print(menge) # [(1, 1), (2, 4), (3, 9), (4, 16)]

# Die Menge aller Tuple (i, i^2) pythonisch / List comprehesions
menge = [(i, i**2) for i in range(1, 5)]
print(menge)


# Beispiel: Filterung mit einer Bedingung
filtered = [number for number in numbers  if number > 3 and number < 9]
print(filtered)

# Ternärer Operator in C: int i = 10 < 3 ? 5 : 9
# Ternärer Operator in Python: i = 5 if 10 < 3 else 9
a = 200
if a > 3:
    b = 2 
else:
    b = 4
print(b)

b = 2 if a > 3 else 4
print(b)


