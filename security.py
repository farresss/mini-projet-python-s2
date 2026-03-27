from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from cryptography.fernet import Fernet


ph = PasswordHasher()

"""key = Fernet.generate_key()
print(key)""" #pour avoir sa propre cle car je ne partage pas les fichier cle il faut donc cree un fichier cle.key et la mettre dedans

cle = open("cle.key", "rb").read()
fernet = Fernet(cle)

def hash_mdp(mdp_compte):
  return ph.hash(mdp_compte)

def verif_mdp(hash_stock, mdp_compte):
  try:
    ph.verify(hash_stock, mdp_compte)
    return True
  except VerifyMismatchError:
    return False

def chiffrement_mdp(mdp):
  return fernet.encrypt(mdp.encode()).decode()

def dechiffrement_mdp(mdp_chiffre):
  return fernet.decrypt(mdp_chiffre.encode()).decode()
    
