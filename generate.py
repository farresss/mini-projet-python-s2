import secrets
import string as s
import csv

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