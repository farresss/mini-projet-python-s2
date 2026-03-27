import tkinter as tk
from auth import login, create_user
from tkinter import ttk
from sites import sites

fenetre = tk.Tk()
fenetre.title("Gestionnaire de mot de passe")
fenetre.geometry("500x800")

label_bienvenue = tk.Label(fenetre, text="Bienvenue sur votre gestionnaire de Mot de Passe")
label_bienvenue.pack()

label_email = tk.Label(fenetre, text="Email")
label_email.pack()

entry_email = tk.Entry(fenetre)
entry_email.pack()

label_mdp = tk.Label(fenetre, text="Mot de Passe")
label_mdp.pack()
entry_mdp = tk.Entry(fenetre, show="*")
entry_mdp.pack()



def connexion():
  email = entry_email.get()
  mdp = entry_mdp.get()

  user = login(email, mdp)

  if user:
    page_accueil()
  else: 
    label_erreur_co = tk.Label(fenetre, text="Email ou mot de passe incorrect", foreground="red")
    label_erreur_co.pack()

def page_accueil():

  for widget in fenetre.winfo_children():
    widget.destroy()
  
  tk.Label(fenetre, text="Menu").pack()

  tk.Button(fenetre, text="Générer un mot de passe", command=page_genere_mdp).pack()
  tk.Button(fenetre, text="Afficher un mot de passe").pack()
  tk.Button(fenetre, text="Modifier un mot de passe").pack()
  tk.Button(fenetre, text="Se connecter à un site").pack()

def page_genere_mdp():
  for widget in fenetre.winfo_children():
    widget.destroy()
    
  n = tk.StringVar()
  site_dispo = ttk.Combobox(fenetre, textvariable=n)
  site_dispo["values"] = list(sites.keys())
  site_dispo.pack()


log = tk.Button(fenetre, text = "Se connecter", command=connexion)
log.pack()
fenetre.mainloop()

