import sqlite3
from os.path import abspath, dirname, join

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Ühendus on olemas!")
        return connection
    except sqlite3.Error as e:
        print(f"Tekkis viga: {e}")
        return connection

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Päring teostatud edukalt.")
    except sqlite3.Error as e:
        print(f"Tekkis viga: {e}")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"Tekkis viga: {e}")

def execute_insert_query(connection, table, data):
    try:
        cursor = connection.cursor()
        placeholders = ', '.join(['?' for _ in data])
        columns = ', '.join(data.keys())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor.execute(query, list(data.values()))
        connection.commit()
        print("Andmed edukalt sisestatud.")
    except sqlite3.Error as e:
        print(f"Tekkis viga: {e}")

def drop_table(connection, table):
    try:
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        connection.commit()
    except sqlite3.Error as e:
        print(f"Tekkis viga: {e}")

create_user_table = """
CREATE TABLE IF NOT EXISTS users(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Lname TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Birthday DATETIME,
    Car TEXT NOT NULL,
    Gender TEXT
)
"""

insert_users = """
INSERT INTO
users(Name, Lname, Age, Birthday, Car, Gender)
VALUES
('Mati', 'Tamm', 50, '2004-07-04', 'auto', 'mees'),
('Karl', 'Puol', 50, '2004-07-04', 'auto', 'mees'),
('Markus', 'Puu', 50, '2004-07-04', 'auto', 'mees'),
('Stefan', 'Mürk', 50, '2004-07-04', 'auto', 'mees')
"""

create_user_auto_table = """
CREATE TABLE IF NOT EXISTS users_auto(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Lname TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Car TEXT NOT NULL,
    varv TEXT NOT NULL,
    number TEXT NOT NULL
)
"""

insert_users_auto = """
INSERT INTO
users_auto(Name, Lname, Age, Car, varv, number)
VALUES
('Mati', 'Tamm', 50, 'Audi', 'Must', '643'),
('Karl', 'Puol', 50, 'BMW', 'Sinnine', '887'),
('Markus', 'Puu', 50, 'Volvo', 'Punane', '213'),
('Stefan', 'Mürk', 50, 'Honda', 'kolane', '904')
"""

select_users = "SELECT * FROM users"

filename = abspath(__file__)
dbdir = dirname(filename)
dbpath = join(dbdir, "data.db")
conn = create_connection(dbpath)

execute_query(conn, create_user_table)
execute_query(conn, insert_users)

user_data = {
    'Name': input("Eesnimi: "),
    'Lname': input("Perekonnanimi: "),
    'Age': int(input("Vanus: ")),
    'Car': input("Auto: "),
    'varv': input("Auto värv: "),
    'number': input("Auto number: ")
}
execute_insert_query(conn, 'users', user_data)

users = execute_read_query(conn, select_users)
print("Kasutajate tabel:")
for user in users:
    print(user)

    #удалить пользователя
def delete_user(connection, table, user_id):
    try:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE Id={user_id}")
        connection.commit()
        print("Kasutaja edukalt kustutatud.")
    except sqlite3.Error as e:
        print(f"Tekkis viga: {e}")

delete_user(conn, 'users', 50)  #удалит пользователя с идентификатором (id) из таблицы "users".

users = execute_read_query(conn, select_users)
print("Kasutajate tabel:")
for user in users:
    print(user)