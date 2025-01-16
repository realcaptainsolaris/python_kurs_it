"""
String Slicing in Python

String Slicing erlaubt es, Teilstrings (Substrings) aus einem String zu
extrahieren.
Mit Hilfe von Start-, End- und Schrittwerten kann flexibel auf bestimmte
Abschnitte eines Strings zugegriffen werden.

Themenübersicht:
1. Grundlagen des Slicings
2. Negative Indizes
3. Slicing mit Schrittwerten
4. Nützliche Anwendungen

Die Slice-Notation
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String
"""

# 1. Grundlagen des Slicings
# Slicing wird mit der Syntax `string[start:end]` durchgeführt.
text = "Python Programmierung"

# Extrahieren eines Teilstrings
print(text[0:5])  # Pytho
print(text[2:6])  # thon

# Wenn der Start- oder Endwert weggelassen wird, wird der Anfang bzw.
# das Ende des Strings verwendet.
print(text[:5])  # Pytho
print(text[5:])  # n Programmierung

# 2. Negative Indizes
# Mit negativen Indizes kann vom Ende des Strings aus zugegriffen werden.

# Slicing mit negativen Indizes
print(text[-12:])  # ogrammierung

# 3. Slicing mit Schrittwerten
# Die Syntax `string[start:end:step]` ermöglicht das Überspringen von
# Zeichen im String.
numbers = "123456789"
print(numbers[::2])  # alle ungeraden Zahlen 
print(numbers[1::2])  # alle geraden Zahlen
print(numbers[::-1])  # 987654321


# 4. Nützliche Anwendungen
# - Extrahieren eines Präfixes oder Suffixes
# - Rückwärtslesen eines Strings
# - Teile von Strings verarbeiten oder analysieren

data = "12345-67890"


# # Übung
# # Schneide jeweils alle A aus den Strings
# AAAAB => AAAA
# BBAAABBB => AAA
# AAAABBBB => AAAA
# ABBBBB => A
string = "AAAAB"
print("AAAAB => AAAA: ", string[:-1])

string = "BBAAABBB"
print("BBAAABBB => AAA: ", string[2:5])

string = "AAAABBBB"
print("AAAABBBB => AAAA: ", string[:-4])

string = "BBAABBBB"
print("BBAABBBB => AA: ", string[2:-4])

string = "ABBBBB"
print("ABBBBB => A: ", string[:1])
