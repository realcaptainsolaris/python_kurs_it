"""
sqlite3: 
"""
import sqlite3

# Verbindung zur Datenbank herstellen
connection = sqlite3.connect("beispiel.db")

# Cursor, um SQL Befehle auszuführen
cursor = connection.cursor()

# Player Table erstellen
cursor.execute("""
CREATE TABLE if not exists players(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER       
)
""")

cursor.execute("INSERT INTO players (name, age) VALUES (?, ?)",
("Bob", 24)
)

# Abfeuern der SQL Anfragen
connection.commit()

# Alle Nutzer auflisten
cursor.execute(
    "SELECT * from players"
)
all_playes = cursor.fetchall()  # alle player holen
print(type(all_playes))
for player in all_playes:
    print(player)


# Datenbank Verbindung muss immer geschlossen werden
connection.close()
