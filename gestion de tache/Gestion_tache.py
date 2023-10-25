import json
import os
import tkinter as tk

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "taches.json")
taches = []

# Toutes les fonctions
def ad_taches():
    nom = entry_nom.get()
    description = entry_description.get()
    date_limite = entry_date_limite.get()
    if nom:
        tache = {
            "nom": nom,
            "description": description,
            "date_limite": date_limite
        }
        taches.append(tache)
        liste_taches.insert(tk.END, f"{nom} - {date_limite}")
        entry_nom.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        entry_date_limite.delete(0, tk.END)
        sauvegarder_taches()

def tache_finit():
    selection = liste_taches.curselection()
    for i in selection:
        liste_taches.itemconfig(i, {'bg': 'light green'})

def supprimer_tache():
    selection = liste_taches.curselection()
    if selection:
        index = selection[0]  
        liste_taches.delete(index)
        if index < len(taches):
            taches.pop(index) 
            sauvegarder_taches()



def sauvegarder_taches():
   with open(json_path, "w") as file:
        json.dump(taches, file)

def afficher_dans_terminal():
    selection = liste_taches.curselection()
    if selection:
        index = selection[0]
        tache = taches[index]
        print("------------------lux :)-------------------------")
        print("Nom de la tâche :", tache["nom"])
        print("Description de la tâche :", tache["description"])
        print("Date limite :", tache["date_limite"])
        print("------------------lux :)-------------------------")


# création de la fenêtre pour l'interface :)
fenetre = tk.Tk()
fenetre.title("GESTIONNAIRE DE TÂCHES DE LUX")
fenetre.geometry("500x400")

# ajout des tâches :)
placeholder = tk.Label(fenetre, text="Nom de la tâche:")
placeholder.pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

placeholder1 = tk.Label(fenetre, text="Description de la tâche:")
placeholder1.pack()
entry_description = tk.Entry(fenetre)
entry_description.pack()

placeholder2 = tk.Label(fenetre, text="Date limite")
placeholder2.pack()
entry_date_limite = tk.Entry(fenetre)
entry_date_limite.pack()

bouton_ajout = tk.Button(fenetre , text="Ajouter" , command=ad_taches)
bouton_ajout.pack()

# affichage des tâches :)
liste_taches = tk.Listbox(fenetre , bg="#E0D8EE")
liste_taches.pack()

#  bouton terminer et supprimer
bouton_finit = tk.Button(fenetre , text="Terminer" , command=tache_finit)
bouton_finit.pack()

bouton_supp = tk.Button(fenetre , text="supprimer" , command=supprimer_tache)
bouton_supp.pack()

# Bouton pour afficher dans le terminal
bouton_afficher = tk.Button(fenetre , text="Afficher dans le terminal" , command=afficher_dans_terminal)
bouton_afficher.pack()

# Charger les tâches depuis le fichier
try:
    with open(json_path, "r") as file:
        taches = json.load(file)
        for tache in taches:
             if 'date_limite' in tache:
                     liste_taches.insert(tk.END, f"{tache['nom']} - {tache['date_limite']}")
             else:
        # Gérer le cas où 'date_limite' est manquant (par exemple, en affichant "Date limite inconnue" ou autre)
                liste_taches.insert(tk.END, f"{tache['nom']} - Date limite inconnue")

except (FileNotFoundError, json.JSONDecodeError):
    pass

# OUVERTURE !
fenetre.mainloop()