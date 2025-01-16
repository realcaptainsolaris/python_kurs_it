"""
Das Thema dieser Datei ist die Verwendung der speziellen Methoden
`__str__` und `__repr__` in Python.

- `__str__` definiert eine benutzerfreundliche Darstellung eines Objekts.
- `__repr__` definiert eine detaillierte und entwicklerfreundliche Darstellung.
- Beide Methoden sind hilfreich, um Objekte besser zu visualisieren und zu debuggen.
"""

# Beispiel 1: Verwendung von __str__


class Person:
    """Eine Klasse, die eine Person repräsentiert."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """String-Repräsentation.
        Wie wird das Objekt repräsentiert, wenn es ausgedruckt wird.
        """
        return f"{self.name}, {self.age}"

    def __repr__(self) -> str:
        """String-Repräsentation für Debuggin.
        Die wird zb. aufgerufen, wenn sich das Objekt in Containter (zb. listen) befindet.
        """
        return f"Person('{self.name}', {self.age})"


otto = Person("otto", 34)
grumpy = Person("Grumpy", 88)
print(otto) # <__main__.Person object at 0x0000016E4D9A6A50>


# Beispiel 2: Verwendung von __repr__
personen = [otto, grumpy]

print(personen)

