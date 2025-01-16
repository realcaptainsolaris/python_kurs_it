"""
Das Thema dieser Datei ist die Kapselung (Encapsulation) in der
objektorientierten Programmierung (OOP) in Python.

- Kapselung bedeutet, dass Attribute und Methoden eines Objekts verborgen
  werden, um sie vor unberechtigtem Zugriff zu schützen.
- Dies wird durch Zugriffsmodifikatoren wie privat (`__`) oder geschützt (`_`) erreicht.
- Getter- und Setter-Methoden erlauben kontrollierten Zugriff auf Attribute.
"""

# Beispiel 1: Verwendung von privaten Attributen


class BankAccount:
    """Eine Klasse, die ein Bankkonto repräsentiert."""

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.kontostand = balance
        # self.__balance = balance  # Privates Attribut
    
    @property
    def kontostand(self):
        return self._kontostand

    @kontostand.setter
    def kontostand(self, new_value):
        if isinstance(new_value, (int, float)):
            self._kontostand = new_value
        else:
            raise ValueError("Das ist keine zahl!")

    # def get_kontostand(self):
    #     return self.kontostand
    
    # def set_kontostand(self, new_value):
    #     if isinstance(new_value, (int, float)):
    #         self.kontostand = new_value

    
    

# Beispielaufrufe der Klasse BankAccount
account = BankAccount("Fischer", "200")
account.kontostand = 332 # setter wird benötigt, um Eingabe/Setzen zu Validieren
print(account.kontostand)  # get

# Beispiel 2: Verwendung von geschützten Attributen


class Employee:
    """Eine Klasse, die einen Mitarbeiter repräsentiert."""

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # Geschütztes Attribut


# Beispielaufrufe der Klasse Employee

# Aufgabe:
# Experimentiere mit ungültigen Gehaltswerten, und beobachte die Reaktion der Methode.

# Beispiel 3: Kombination von Kapselung mit Eigenschaften (Properties)


class Product:
    """Eine Klasse, die ein Produkt repräsentiert."""


# Beispielaufrufe der Klasse Product

# Aufgabe:
# Versuche, einen ungültigen Preis zu setzen, und beobachte die Exception.
