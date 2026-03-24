import sqlite3

connection = sqlite3.connect("mdp.db")
connection.execute("PRAGMA foreign_keys = 1")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (id_user INTEGER PRIMARY KEY, 
               email TEXT,
               mdp_compte TEXT);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS mdp (id_mdp INTEGER PRIMARY KEY,
                mdp TEXT,
                location TEXT,
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES user (id_user)); ''')
connection.commit()


