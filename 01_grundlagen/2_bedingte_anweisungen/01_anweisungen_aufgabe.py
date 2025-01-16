"""
Schreibe ein Programm, welches die Usereingabe nach folgenden Kriterien prüft:

- Die Eingabe darf kein Leerzeichen enthalten
- Die Eingabe muss mindestens ein großes "A" enthalten, allerdings nicht an Index 0
- die Eingabe muss mindestens drei Zeichen lang sein.

Wenn die Eingabe den Kriterien entspricht, soll eine entsprechende Meldung ausgegeben werden.
Wenn die Eingabe nicht den Kriterien entspricht, soll eine entsprechende Meldung ausgegeben werden.

Hinweise:
----------
- verwende die Methode find um zu prüfen, ob ein "A" enthalten ist.
- Verwende den in-Operator um zu prüfen, ob ein Leerzeichen enthalten ist.
- Verwende die Methode len() um die Länge der Eingabe zu prüfen.

Beispiel:
-------------
Bitte geben Sie ein Wort ein: rAbe
Ihre Eingabe ist korrekt.

Bitte geben Sie ein Wort ein: ol
Ihre Eingabe ist leider falsch.

Bitte geben Sie ein Wort ein: Aber
Ihre Eingabe ist leider falsch.
"""

eingabe = input("Bitte gebe ein gültiges Wort ein: ")

if eingabe.find(" ") > -1 or eingabe.find("A") < 1 or len(eingabe) < 3:
    print("Ihre Eingabe war: ", eingabe)
    print("Ihre Eingabe ist leider falsch.")
else:
    print("Ihre Eingabe ist korrekt.")

print(eingabe.find("A"))  # 2