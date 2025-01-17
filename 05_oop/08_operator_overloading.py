"""
Operator Overloading (Operatorüberladung)

- Operatorüberladung ermöglicht es, die Standardfunktionen von Operatoren
  (z. B. +, -, *) für benutzerdefinierte Klassen zu definieren.
- Dies wird durch das Implementieren spezieller Methoden wie `__add__`, `__sub__`,
  und `__mul__` erreicht.
- Es erhöht die Lesbarkeit und Flexibilität von benutzerdefiniertem Code.
"""
class A:
    def __len__(self):
        # Implementierung der Länge in der Klasse A
        return 2
    
    def __getitem__(self, key):
        return "hallo welt"

a = A()
print("Länge von a:", len(a))  # ruft __len__() auf
print(a["irgendwas"])


# Länge einer Liste
x = [1, 2, 3]
print(len(x))



# Beispiel 1: Überladen des Addition-Operators


class Vector:
    """Eine Klasse, die einen mathematischen Vektor repräsentiert."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Addiere zwei Vektoren."""
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
    
    def __str__(self):
        return f"Vector: {self.x} / {self.y}"


v1 = Vector(10, 123)
v2 = Vector(2, 5)
v3 = v1 + v2
print(v3)


# Beispiel 2: Überladen des Multiplikationsoperators


class Matrix:
    """Eine Klasse, die eine einfache Matrix repräsentiert."""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        """Definiert die Darstellung der Matrix."""
        return f"Matrix({self.value})"


# Beispielaufrufe
m1 = Matrix([[1, 2], [3, 4]])


# Beispiel 3: Überladen von Vergleichsoperatoren


class Box:
    """Eine Klasse, die eine Box mit einem Volumen repräsentiert."""

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def volume(self):
        """Berechnet das Volumen der Box."""
        return self.width * self.height * self.depth


# Beispielaufrufe
b1 = Box(2, 3, 4)
b2 = Box(3, 3, 3)
