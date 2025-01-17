import sqlite3

# Verbindung zur Datenbank herstellen
# connection = sqlite3.connect("beispiel.db")

# Cursor, um SQL Befehle auszuführen
# cursor = connection.cursor()
def insert_user(connection, cursor, data):
    cursor.execute(
        "INSERT INTO players (name, age) VALUES (?, ?)",
        data
    )
    connection.commit()

def update_age(connection, cursor, id_, new_age):
    cursor.execute(
        "UPDATE players set age=? WHERE id=?",
        (new_age, id_)
    )
    connection.commit()


def get_user_by_id(cursor, id_):
    cursor.execute("SELECT * from players where id=?", (id_,))
    user = cursor.fetchone()
    return user


def get_users(cursor):
    cursor.execute("SELECT * from players")
    return cursor.fetchall()


# with kümmert sich selbständig um das schließen
with sqlite3.connect("beispiel.db") as conn:
    cursor = conn.cursor()
    data = ["Alice", 34]
    insert_user(conn, cursor, data)
    update_age(conn, cursor, 4, 42)
    user = get_user_by_id(cursor, 4)
    print(user)