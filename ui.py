import tkinter as tk


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

log = tk.Button(fenetre, text = "Se connecter")
log.pack()
fenetre.mainloop()

