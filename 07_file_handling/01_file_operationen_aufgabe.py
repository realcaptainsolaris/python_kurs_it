"""
Praktische Aufgabe: Datei auslesen

Aufgabe:
Erstelle eine Textdatei mit dem Namen "text.txt" und folgendem Inhalt:

--- Inhalt von text.txt ---
Python ist eine vielseitige Programmiersprache.
Sie wird für Webentwicklung, Datenanalyse und KI verwendet.
Python ist einfach zu lernen.
--- Ende ---

Schreibe ein Python-Programm, das die Datei "text.txt" einliest
und den Inhalt zeilenweise ausgibt.

Bonus:
- Zähle die Anzahl der Wörter in der Datei.
- Gib die längste Zeile aus.
"""

from pathlib import Path


def read_lines(file_path):
    """Liest den Inhalt einer Datei zeilenweise aus."""
    lines = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())
    return lines

def finde_wortanzahl(zeilen):
    """Zählt die Anzahl der Wörter in einer Liste von Zeilen."""
    c = 0
    for zeile in zeilen:
        c += len(zeile.split())
    print(c)


def finde_laengste_zeile(zeilen):
    """Findet die längste Zeile in einer Liste von Zeilen."""
    ...


def main():
    file_path = Path(__file__).parent / "text.txt"

    # Gib den Inhalt zeilenweise aus
    print("Inhalt der Datei:")
    zeilen = read_lines(file_path)  # einer Liste von Strings
    print(zeilen)


    # Bonus 1: Zähle die Anzahl der Wörter
    wortanzahl = finde_wortanzahl(zeilen)
    print("\nAnzahl der Wörter:", wortanzahl)


    # Bonus 2: Finde die längste Zeile
    laengste_zeile = finde_laengste_zeile(...)

main()