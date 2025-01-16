"""
Python Variablen und Dateinamen: Konventionen und Best Practices

In Python ist es wichtig, sowohl bei der Benennung von Variablen als auch
bei Dateinamen klare und konsistente Konventionen zu verwenden. Dadurch
wird der Code lesbarer, verständlicher und einfacher zu warten.

Konventionen:
- Variablennamen:
  - Verwenden Sie Kleinbuchstaben und Unterstriche (snake_case).
  - Vermeiden Sie reservierte Schlüsselwörter oder Namen, die leicht mit
    integrierten Funktionen verwechselt werden können (z. B. `list`, `str`).
  - Namen sollten aussagekräftig sein und den Zweck der Variable
    beschreiben.
  - Variablen dürfen nicht mit einer Zahl beginnen.

- Dateinamen:
  - Verwenden Sie ebenfalls snake_case.
  - Namen sollten beschreiben, was das Skript tut oder wofür es gedacht
    ist.
  - Keine Sonderzeichen oder Leerzeichen in Dateinamen verwenden.
  - Modulnamen sollten nicht mit einer Zahl beginnen, wenn sie später
    importiert werden sollen

Der Python Styleguide heisst PEP 8 und enthält unter anderem Empfehlungen zur
Benennung von Variablen und Dateinamen.

https://peps.python.org/pep-0008/
"""

# Beispiel für Variablennamen
# Hier werden Variablen mit sinnvollen und konsistenten Namen erstellt
user_name = "Bob"  # Snake-Case: klein und Underscore
distance_total = 100

# Beispiel für schlechte Variablennamen
# Vermeiden Sie Namen wie diese:
a = "Alice"
print(type(a)) # a ist ein Objekt der Klasse String

# 0_name = ""  illegaler Name, da mit Zahl anfängt
# mein name : illegaler Name, da Leerzeichen

# Beispiel für Dateinamen auch in Snake-Case
# Gute Beispiele: my_script.py, calculate_savings.py, data_analysis.py
# Schlechte Beispiele: script1.py, temp.py, 123.py


