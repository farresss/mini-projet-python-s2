from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from cryptography.fernet import Fernet


ph = PasswordHasher()

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
    
