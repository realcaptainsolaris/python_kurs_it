""" 
Path und File Operationen
"""
from pathlib import Path 


print(__file__)  # absoluter Pfad zu der Datei im Dateisystem

pathobject = Path(__file__)
print(pathobject.parent / "data" / "config.txt")

zip_object = zip([1,2], ["a", "b"])  # erzeugt einen Iterator
print(next(zip_object))


# Datei auslesen (effizienteste Methode)
with open(pathobject.parent / "data" / "config.txt", mode="r") as f:
    # f.read() # f ist filehandle, und zusätzlich ein Zeilen-Iteror
    #print(next(f))
    for line in f:
        print(line)