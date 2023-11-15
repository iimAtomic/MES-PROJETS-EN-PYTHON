import json
import os
import tkinter as tk


#pour que le fichier se charge dans le repertoire du fichier py du projet 
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "contacts.json")
contacts = []

# Toutes les fonctions
def ad_contacts():
    nom = entry_nom.get()
    numero = entry_numero.get()
    Prenom = entry_Prenom.get()
    if nom:
        contact = {
            "nom": nom,
            "numero": numero,
            "Prenom": Prenom
        }
        contacts.append(contact)
        liste_contacts.insert(tk.END, f"{nom} - {Prenom}")
        entry_nom.delete(0, tk.END)
        entry_numero.delete(0, tk.END)
        entry_Prenom.delete(0, tk.END)
        sauvegarder_contacts()



def supprimer_contact():
    selection = liste_contacts.curselection()
    if selection:
        index = selection[0]  
        liste_contacts.delete(index)
        if index < len(contacts):
            contacts.pop(index) 
            sauvegarder_contacts()



def sauvegarder_contacts():
   with open(json_path, "w") as file:
        json.dump(contacts, file)

def afficher_dans_terminal():
    selection = liste_contacts.curselection()
    if selection:
        index = selection[0]
        contact = contacts[index]
        print("------------------lux :)-------------------------")
        print("Nom de la tâche :", contact["nom"])
        print("numero de la tâche :", contact["numero"])
        print("Date limite :", contact["Prenom"])
        print("------------------lux :)-------------------------")

def afficher_dans_liste():
    selection = liste_contacts.curselection()
    if selection:
        index = selection[0]
        contact = contacts[index]
        liste_cont.insert(tk.END, contact["nom"] - contact["Prenom"])
           
    


# création de la fenêtre pour l'interface :)
fenetre = tk.Tk()
fenetre.title("GESTIONNAIRE DE TÂCHES DE LUX")
fenetre.geometry("500x500")

# ajout des tâches :)
placeholder = tk.Label(fenetre, text="Nom du contact:")
placeholder.pack()
entry_nom = tk.Entry(fenetre)
entry_nom.pack()

placeholder1 = tk.Label(fenetre, text="numero du contact")
placeholder1.pack()
entry_numero = tk.Entry(fenetre)
entry_numero.pack()

placeholder2 = tk.Label(fenetre, text="prénom du contact")
placeholder2.pack()
entry_Prenom = tk.Entry(fenetre)
entry_Prenom.pack()

bouton_ajout = tk.Button(fenetre , text="Ajouter" , command=ad_contacts)
bouton_ajout.pack()

#  bouton voir et supprimer


bouton_voir = tk.Button(fenetre , text="voir" , command=afficher_dans_liste)


bouton_supp = tk.Button(fenetre , text="supprimer" , command=supprimer_contact)


# Bouton pour afficher dans le terminal
bouton_afficher = tk.Button(fenetre , text="Afficher dans le terminal" , command=afficher_dans_terminal)
bouton_ajout = tk.Button(fenetre, text="Ajouter", command=ad_contacts)
bouton_ajout.pack(side=tk.LEFT)

bouton_voir = tk.Button(fenetre, text="Voir", command=afficher_dans_liste)
bouton_voir.pack(side=tk.LEFT)

bouton_afficher = tk.Button(fenetre, text="Afficher dans le terminal", command=afficher_dans_terminal)
bouton_afficher.pack(side=tk.LEFT)

# affichage des tâches :)
frame_listbox = tk.Frame(fenetre, padx=20, pady=20)
frame_listbox.pack()

liste_contacts = tk.Listbox(frame_listbox , bg="#EAE7C3" , width=200 , height=100 )
liste_contacts.pack()


# Charger les contacts depuis le fichier
try:
    with open(json_path, "r") as file:
        contacts = json.load(file)
        for contact in contacts:
             if 'Prenom' in contact:
                     liste_contacts.insert(tk.END, f"{contact['nom']} - {contact['Prenom']}")
             else:
        # Gérer le cas où 'Prenom' est manquant (par exemple, en affichant "prenom inconnu" ou autre)
                liste_contacts.insert(tk.END, f"{contact['nom']} - prenom inconue")

except (FileNotFoundError, json.JSONDecodeError):
    pass

# OUVERTURE !
fenetre.mainloop()