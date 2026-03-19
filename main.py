import secrets
import string as s
import csv
import sqlite3

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
               username TEXT);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS mdp (id_mdp INTEGER PRIMARY KEY,
                mdp TEXT,
                location TEXT,
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES user (id_user)); ''')
connection.commit()

print(connection.total_changes)



#sauvegarde_mdp("test2", "ent", generer_mdp(20))