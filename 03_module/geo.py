""" 
Modul für Geometrie Funktionen
"""
import math


def distance(p1: tuple, p2: tuple) -> float:
    """Distanz zweier Punkte in der euklidischen Ebene."""
    return math.dist(p1, p2)
