from db import cursor, connection
from security import dechiffrement_mdp, chiffrement_mdp

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