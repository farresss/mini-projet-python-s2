import secrets
import string as s
import csv
import sqlite3
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from cryptography.fernet import Fernet

ph = PasswordHasher()

cle = open("cle.key", "rb").read()
fernet = Fernet(cle)

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

def chiffrement_mdp(mdp):
  return fernet.encrypt(mdp.encode()).decode()

def dechiffrement_mdp(mdp_chiffre):
  return fernet.decrypt(mdp_chiffre.encode()).decode()

def create_user(email, mdp_compte):
  mdp_hash = ph.hash(mdp_compte)
  cursor.execute("INSERT INTO user (email, mdp_compte) values (?, ?);", (email, mdp_hash))
  connection.commit()

def login(email, mdp_compte):
  cursor.execute("SELECT id_user, mdp_compte FROM user WHERE email = ?", (email,))
  row =  cursor.fetchone()
  if row != None:
    id_user =  row[0]
    hash_stock = row[1]
    try:
      ph.verify(hash_stock, mdp_compte)
      return id_user
    except VerifyMismatchError:
      return False
  else:
    return False
  
def add_mdp(mdp, location, id_user):
  
  cursor.execute("INSERT INTO mdp (mdp, location, id_user) VALUES (?, ?, ?)", (chiffrement_mdp(mdp), location, id_user))
  connection.commit()

def get_mdp(location, id_user):
  cursor.execute("SELECT mdp FROM mdp WHERE location = ? AND id_user = ? ", (location, id_user))
  row =  cursor.fetchone()
  if row != None:
    return dechiffrement_mdp(row[0])
  else:
    return False
  
def modifier_mdp(mdp, location, id_user):
  
  new_mdp = chiffrement_mdp(mdp)
  cursor.execute("UPDATE mdp SET mdp = ? WHERE location = ? AND id_user = ?", (new_mdp, location, id_user))
  connection.commit()


'''create_user("test@test.gmail.com", "mdp123")
print(login("test@test.gmail.com", "mdp123"))
print(login("test@test.gmail.com", "123333"))'''













#print(connection.total_changes)
#sauvegarde_mdp("test2", "ent", generer_mdp(20))