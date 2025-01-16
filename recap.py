""" 
Recap 3 Tage
"""
# unveränderliche Datentypen
x = 3 
y = 3.3
name = "bob" # sequenz
t = (1, 2) # tuple
t2 = 1, 2  # tuple ohne runden klammern

a, b = t2  # tuple entpacken

print(x.bit_length())  # unveränderl. Datentypen erzeugen IMMER einen neuen Wert
lower_case_name = name.lower()

# veränderlichen Datentypen
names = ["Bob", "Alice"]
names.pop() # erzeugen manchmal einen neuen Wert
names.sort() # sortiert inplace, erzeugt keinen neuen Wert

d = {"a": [1, 2]}

# Loops
for index, name in enumerate(names, start=11):
    print(index, name)

# Funktionen mit paramentern a und b und type-hints
def fn(a: int, b: str, c: list[int]) -> list:
    print(a, b)
    return [1, 2]

def g(device: str, force: bool) -> None:
    ...

def defaultfun(a, b, c=3):
    print(a, b, c)
    

x = fn(3, "hallo", [1, 2, 3])
g(device="mx2", force=False)

defaultfun(1, 2)    # c wird mit 3 belegt
defaultfun(1, 2, 4) # 4 überschreibt c


