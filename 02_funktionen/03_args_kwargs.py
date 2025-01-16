"""
Das Thema dieser Datei ist `*args`, `**kwargs` und Default-Parameter.
- `*args` erlaubt eine unbestimmte Anzahl an positionsbasierten Argumenten.
- `**kwargs` erlaubt eine unbestimmte Anzahl an keywordbasierten Argumenten.
- Default-Parameter können standardisierte Werte festlegen, die verwendet
  werden, wenn kein Argument übergeben wird.
"""

def fn_default(a, b, c=42):
    print(f"fn default: {a=}, {b=}, {c=}")


fn_default(2, 3)  # fn default: a=2, b=3, c=42
fn_default(2, 3, 99)  # fn default: a=2, b=3, c=99


# Definition einer Funktion mit `*args`
def fn_args(a, b, *args):
    # args sammelt alle positionellen Argumente auf in einem Tupel
    print(a, b) # 2 17
    print(args) # ((3, 4), 34, 2, 55, 21, 8)


fn_args(2, 17, (3,4), 34, 2, 55, 21, 8)


def load_csv(filename, encoding):
    print(filename, encoding)


load_csv(encoding="utf-8", filename="data/data.csv") # Keyword Arguments


# Beispielaufruf der Funktion

# Definition einer Funktion mit `**kwargs`
def configure_device(start, machine_name, **kwargs):
    print(kwargs)
    print(start, machine_name)
    if "shutdown" in kwargs:
        print("shut down")
    if "timeout" in kwargs:
        print("timeout")
    

# Beispielaufruf der Funktion
configure_device(True, "C34", timeout=23, force=True, shutdown=True)


# Kombination von `*args`, `**kwargs` und Default-Parametern

def func(*args, **kwargs):
    print(args, kwargs)
  
func(1, 2, 3, x=2, y=3, z=4)

