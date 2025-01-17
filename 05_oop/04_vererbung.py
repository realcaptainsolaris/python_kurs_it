"""
Das Thema dieser Datei ist die Vererbung in der objektorientierten
Programmierung (OOP) in Python.

- Vererbung erlaubt es, Eigenschaften und Methoden einer Basisklasse
  (Elternklasse) auf abgeleitete Klassen (Kindklassen) zu übertragen.
- Sie fördert Wiederverwendung und Erweiterbarkeit von Code.
- Die Basisklasse wird mit `class ChildClass(ParentClass):` vererbt.
"""

# Beispiel 1: Grundlagen der Vererbung


class Animal:
    """Basisklasse, die allgemeine Eigenschaften von Tieren definiert."""
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        self.is_alive = True

    def say(self):
        print(f"{self.name} says nothing, aber ist am Leben: {self.is_alive}")



# Kindklasse, die von Animal erbt
class Duck(Animal):

    def __init__(self, name, age, federgewicht):
        super().__init__(name, age)
        self.federgewicht = federgewicht

    # def say(self):
    #     print(f"{self.name} says Qauck Quack")


# Kindklasse, die von Animal erbt
class Dog(Animal):
    pass 


donald = Duck("Donald", 120, "weich")
donald.say()


##################################
class Rectangle:
    def __init__(self, a, b):
        self.a = a 
        self.b = b 

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)


r = Rectangle(3, 5)
print("Fläche von r:", r.area())

s = Square(3)
s.area()



# Aufgabe:
# Füge eine weitere Kindklasse hinzu, z. B. Bird, und implementiere eine
# spezifische `speak`-Methode.

# Beispiel 2: Verwendung der Basisklasse mit `super()`


class Vehicle:
    """Basisklasse für Fahrzeuge."""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def description(self):
        """Gibt eine Beschreibung des Fahrzeugs zurück."""
        return f"Fahrzeug: {self.brand} {self.model}"


# Kindklasse, die die Basisklasse erweitert


# Beispielaufruf der Klasse Car

# Beispiel 3: Typprüfung mit `isinstance` und `issubclass`
# print(isinstance(dog, Animal))  # True
# print(isinstance(dog, Dog))  # True
# print(issubclass(Dog, Animal))  # True
# print(issubclass(Cat, Dog))  # False
