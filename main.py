import secrets
import string as s
import csv
import sqlite3
import hashlib

def generer_mdp(taille, majuscule = True, chiffre = True, car_spec = True):
  char = s.ascii_lowercase
  mdp = ""
 
  if majuscule:
    char += s.ascii_uppercase

  if chiffre:
    char += s.digits

  if car_spec:
    char += s.punctuation
  
  for _ in range(taille):
    '''if i == taille // 3 or i == (taille // 3) * 2:
      mdp += "-"''' #Au cas ou si on fait des mdp de 20 et avoir un format de mdp comme apple xxxxxx-xxxxxx-xxxxxx
    v = secrets.choice(char)
    mdp += v

  return mdp

def sauvegarde_mdp(user, location, mdp):

  with open("mdp.csv", "a", newline= "") as f:
    writer = csv.writer(f)
    writer.writerow([user, location, mdp])


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

def hash_mdp(mdp):
  return  hashlib.sha256(mdp.encode()).hexdigest()
def create_user(email, mdp_compte):
  cursor.execute("INSERT INTO user (email, mdp_compte) values (?, ?);", (email, hash_mdp(mdp_compte)))
  connection.commit()

def login(email, mdp_compte):
  cursor.execute("SELECT * FROM user WHERE email = ? AND mdp_compte = ?", (email, hash_mdp(mdp_compte)))
  row =  cursor.fetchone()
  if row != None:
    return row[0]
  else:
    return False
  
def add_mdp(mdp, location, id_user):
  cursor.execute("INSERT INTO mdp (mdp, location, id_user) VALUES (?, ?, ?)", (mdp, location, id_user))
  connection.commit()

def get_mdp(location, id_user):
  cursor.execute("SELECT mdp FROM mdp WHERE location = ? AND id_user = ? ", (location, id_user))
  row =  cursor.fetchone()
  if row != None:
    return row[0]
  else:
    return False

#print(connection.total_changes)



#sauvegarde_mdp("test2", "ent", generer_mdp(20))