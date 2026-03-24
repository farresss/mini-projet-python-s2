from db import cursor, connection
from security import hash_mdp, verif_mdp

def create_user(email, mdp_compte):
  mdp_hash = hash_mdp(mdp_compte)
  cursor.execute("INSERT INTO user (email, mdp_compte) values (?, ?);", (email, mdp_hash))
  connection.commit()

def login(email, mdp_compte):
  cursor.execute("SELECT id_user, mdp_compte FROM user WHERE email = ?", (email,))
  row =  cursor.fetchone()
  if row != None:
    id_user =  row[0]
    hash_stock = row[1]
    if verif_mdp(hash_stock, mdp_compte):
      return id_user
    else:
      return False
    
  return False