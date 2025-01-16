"""
Das Thema dieser Datei ist das Erstellen und Verwenden eigener Module in Python.

- Ein Modul ist eine Datei, die Python-Code enthält (z. B. Funktionen, Klassen).
- Eigene Module helfen dabei, Code besser zu organisieren und wiederzuverwenden.
- Module werden mit `import` in anderen Python-Dateien verwendet.
"""
# import aus der Python Standard-bibliothek
import sys
import random

# Starimport (importiere alles in den Scope). BAD PRACTICE!
from tkinter import *

# from Import 
from pathlib import Path  # import Path-Klasse aus pathlib
from os import abort, access

# Numpy Package: Drittanbietermodul (installiert via: pip install numpy)
import numpy

# Alias import 
import numpy as np

# eigenes Modul geo.py
# import geo
from geo import distance

# Zugriff über Namespace Random (man weiß, woher gauss kommt)
random.gauss(3, 1)

distance((2, 2), (3, 2))
# geo.distance((2, 2), (3, 2)) # zugriff über den namespace geo

# Zugriff auf Pathobjekt OHNE Namespace
Path(__file__)

image_names() # image_names() aus tkinter

# Zugriff auf Random-Modul des Numpy-Packages via alias np
np.random.dirichlet

