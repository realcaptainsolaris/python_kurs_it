"""
Das Thema dieser Datei ist die Arbeit mit Dateioperationen in Python.

- Python bietet zahlreiche Funktionen, um Dateien zu lesen, zu schreiben
  und zu manipulieren.
- Wir betrachten grundlegende Dateioperationen wie das Erstellen, Lesen,
  Schreiben und Löschen von Dateien.
"""

# 1. Datei erstellen und schreiben
from pathlib import Path

file_name = Path(__file__).parent / "example.txt"
DATA_DIR = Path(__file__).parent  # Verzeichnis wo die Datei 01_file_operations liegt.

# Schreiben in eine Datei (überschreibt den Inhalt, falls vorhanden)

# 2. Datei lesen
# Lesen des gesamten Inhalts (encoding angeben)
file_handle = open(DATA_DIR / "oceans.txt", mode="r", encoding="utf-8")
content = file_handle.read()
print(content)
file_handle.close()


# Zeilenweise lesen
# with Kontext-Manager schließt die Datei automatisch close()
new_oceans = []
with open(DATA_DIR / "oceans.txt", mode="r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("A"):
            new_oceans.append(line + "\n")



with open(DATA_DIR / "oceans_neu.txt", mode="w", encoding="utf-8") as f:
    # f.writelines(new_oceans)
    for line in new_oceans:
        f.write(line)


# Lesen und Schreiben
with open(DATA_DIR / "oceans.txt", mode="r", encoding="utf-8") as f, open(DATA_DIR / "oceans_neu2.txt", mode="w", encoding="utf-8") as f2:
    for line in f:
        line = line.strip()
        if line.startswith("A"):
            f2.write(line + "\n")
        


