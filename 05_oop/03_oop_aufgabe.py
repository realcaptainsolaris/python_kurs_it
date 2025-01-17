"""
Vervollständige die Klasse Produkt und lege die entsprechenden Properties an. (MITTEL)

# Es gelten folgende Constraints (Regeln):
- Der Preis darf nicht negativ sein und muss eine Zahl sein
- Die Verfügbarkeit muss den Zustand "in stock" oder "out of stock" haben.
- Im Fehlerfall raise ValueError.

Implementiere auch __str__ und __repr__.

Teste mit folgenden Produkten:
products = [
    ("Maggi", 23.2, "in stock"),
    ("Snickers", 4, "out of stock"),
    ("Petersilie", 1.9, "stock"),  # muss scheitern
    ("Gouda Käse", -12.50, "out of stock"),  # muss scheitern
    ("Za", 23.2, "inn stock"),  # muss scheitern.
]
Nutze zum testen einen Loop und try -except
"""


class Produkt:
    def __init__(self, name, preis, verfuegbarkeit):
        # Hier müssen die Instanzvariablen initialisiert werden
        self.name = name
        self.preis = preis  # self.preis(209)
        self.verfuegbarkeit = verfuegbarkeit

    @property 
    def preis(self):
        return self._preis

    @preis.setter
    def preis(self, value):
        self._preis = value

    def __str__(self) -> str:
        return f"{self.name} kostet {self.preis} und ist {self.verfuegbarkeit}"


if __name__ == "__main__":
    products = [
        ("Maggi", 23.2, "in stock"),
        ("Snickers", 4, "out of stock"),
        ("Petersilie", 1.9, "stock"),  # muss scheitern
        ("Gouda Käse", -12.50, "out of stock"),  # muss scheitern
        ("Za", 23.2, "inn stock"),  # muss scheitern.
    ]

    for product in products:
        try:
            obj = Produkt(*product)
            print(obj)
            # print(obj.preis)  # Default Get-Zugriff
            # obj.preis = -23   # Default set-Zugriff
        except ValueError as e:
            print(f"es ist ein Fehler aufgetreten: {e}")
