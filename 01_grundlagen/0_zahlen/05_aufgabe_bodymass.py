"""
Berechne den Body-Mass-Index: (LEICHT)

Der Body-Mass-Index (kurz: BMI) ist eine Zahl, mit der man abschätzen kann,
ob man Unter-, Normal oder Übergewicht hat. Man berechnet diese Zahl nach der folgenden Formel:

          Gewicht (kg)
BMI = ---------------
       Größe (m) * Größe (m)

WICHTIG:
Dabei wird das Gewicht in kg und die Größe in m angegeben.

AUFGABE:
-----------
über Input wird das Gewicht in Gramm (g) eingegeben und die Höhe in cm. Rechne
die Eingabewerte entsprechend um (zb. g in kg) und berechne das Ergebnis. Lege dafür passende
Variablen an.

Wir gehen von legalem und validem Input aus.
Runde auf zwei Nachkommastellen.

Überprüfen:
Der Body-Mass-Index (BMI) für eine Person, die 95 kg wiegt und 1,80 Meter groß ist, beträgt etwa 29,32.

Beispiel:
------------
Bitte gebe das Gewicht in g ein: 95000
Bitte gebe die Größe in cm ein: 180
Der Body-Mass-Index beträgt: 29.32
"""

weight = int(input("Bitte das Gewicht in Gramm eingeben zb. 95000: "))
height = float(input("Bitte die Grösse in cm eingeben: zb. 180: "))

weight_kg = weight / 1000
height_m = height / 100

# BMI ausrechnen
bmi = round(weight_kg / (height_m**2), 2)
print("BMI: ", bmi)