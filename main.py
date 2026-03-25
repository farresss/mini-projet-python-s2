from auth import login, create_user
from generate import generer_mdp
from password import add_mdp, modifier_mdp, get_mdp
from browser import login_site
import time


email = input("entrez votre email : ")
mdp = input(" entrez votre mdp: ")

id_user = login(email, mdp)

if not id_user:
  print("Email ou mdp incorrect")
  exit()

print("Bienvenue")

while True:
  print("1. Ajouter un mdp")
  print("2. Afficher mdp")
  print("3. Modifier mdp")
  print("4. Lancer un site")
  print("5. Quitter")

  choix = input("Choix: ")

  if choix == "1":
    location = input("Choisir un site:")
    mdp = generer_mdp(20)
    add_mdp(mdp, location, id_user)
    print("Mdp ajouter")
  
  elif choix == "2":
    location = input("Choisir un site:")
    mdp = get_mdp(location, id_user)
    print("Mdp : ", mdp)
  
  elif choix == "3":
    location = input("Choisir un site:")
    mdp = input("Saisir un nouveau mdp")
    modifier_mdp(mdp, location, id_user)
    print("Mdp modifier")
  
  elif choix == "4":
    location = input("Choisir Site : ")
    driver = login_site(location, id_user, email)
    time.sleep(20)
    driver.quit()
    
  elif choix == "5":
    print("Salut")
    break




  


'''create_user("test@test.gmail.com", "mdp123")
print(login("test@test.gmail.com", "mdp123"))
print(login("test@test.gmail.com", "123333"))'''













#print(connection.total_changes)
#sauvegarde_mdp("test2", "ent", generer_mdp(20))