"""
Das Thema dieser Datei ist eine Einführung in die objektorientierte
Programmierung (OOP) in Python.

- OOP konzentriert sich auf die Modellierung von Objekten aus der realen Welt.
- Die Grundkonzepte umfassen Klassen, Objekte, Attribute und Methoden.
"""

x = int("3")  # Erstellen ein Objekt der Klasse Integer
x.denominator  # Attribut
x.to_bytes     # Methode

# Beispiel 1: Definition einer Klasse und Erstellung eines Objekts
class House:
    pass 


# Erstellen eines House-Objekts (Instanziieren)
# Ein Objekt wird auch als Instanz bezeichen
mini_house = House()
print(type(mini_house))  # <class '__main__.House'>

if isinstance(mini_house, House):
    print("Minihaus ist ein Haus")

print("*" * 40)

# Erstellung eines Objekts der Klasse Person
class Person:

    def __init__(self, name: str, age: int) -> None:
        print("wird aufgerufen, wenn Personen-Objekt erstellt wird")
        self.name = name # bob.name = name
        self.age = age

    def say_hello(self):
        print(f"Mein Name ist {self.name} und ich bin {self.age} Jahre alt.")


# Bob objekt
bob = Person(name="Bob", age=23)
print("bob name:", bob.name)
print("bob age:", bob.age)

# Alice objekt
alice = Person(name="Alice", age=34)

# Grumpy Objekt
grumpy = Person("Grumpy", 88)
print(grumpy.name)


# alle Attribute (Eigenschaften) eines Objekts
print(vars(grumpy)) # {'name': 'Grumpy', 'age': 88}


# Zeige alle Methoden von Klasse Person:
# print(dir(Person))


# Beispiel 2: Aktualisieren von Attributen
bob.age += 1
bob.name = "Bobby"
bob.say_hello()
grumpy.say_hello()


# Verwendung der Counter-Klasse
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1 

    def decrement(self):
        self.value -= 1


counter = Counter()  # counter.value = 0
counter2 = Counter()
counter.increment()
counter.increment() # ++
counter.decrement() # --


# ------------------------------------------------------------
# Herkömmlicher Weg eines Counters über global (nicht ratsam)
# globales verändern
# ------------------------------------------------------------
value = 0

def increment():
    global value  
    value += 1

def decrement():
    global value 
    value -= 1


increment()
increment()
decrement()
decrement()
print("vla:", value)


# Beispiel 3: Einfache Datenvalidierung


# Beispielaufruf der Klasse Product
# Aufgabe Klasse Produkt
# Entwerfe eine Klasse Produkt mit den Eigenschaften name, preis und Gewicht
# zb. Nutella, 3.20, 500g
# eine Methode display_info() => soll ausgeben: Nutella, Preis 3,30, 500g
class Product:

    anzahl = 0  # Klassenvariable (gehört zur Klasse und NICHT zur Instanz)

    def __init__(self, name, preis, gewicht):
        self.name = name  # Instanzvariablen / Objekt-Attribute
        self.preis = preis 
        self.gewicht = gewicht 
        Product.anzahl += 1

    def display_info(self):
        print(f"{self.name=} {self.preis=} {self.gewicht=}")


nutella = Product("nutella", 34, "500g")
nutella.display_info()
print(vars(nutella))  # {'name': 'nutella', 'preis': 34, 'gewicht': '500g'}
print(vars(Product))

products = [
    ("nutella", 34, "500g"),
    ("haribo", 12, "100g"),
    ("mozarella", 212, "1000g"),
    ("Bier", 2, "500ml"),
]

# Iterativ aus einer Produktliste Produkte erstellen und in p einhängen
p = []
for product in products:
    name, preis, gewicht = product
    pro = Product(name, preis, gewicht)
    p.append(pro)

print(p)
print("Anzahl der erstellten Produkte:", Product.anzahl)