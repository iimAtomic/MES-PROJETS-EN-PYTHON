import tkinter as tk

def ajouter_caractere(caractere):
    expression_actuelle = entry.get()
    nouvelle_expression = expression_actuelle + caractere
    entry.delete(0, tk.END)
    entry.insert(0, nouvelle_expression)

def effacer():
    entry.delete(0, tk.END)

def calculer():
    expression = entry.get()
    try:
        resultat = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(resultat))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erreur")

# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.geometry("400x400")

# Créer un champ de saisie
entry = tk.Entry(fenetre, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Créer les boutons pour les chiffres et les opérations
chiffres = "1234567890"
ligne = 1
colonne = 0
for caractere in chiffres:
    tk.Button(fenetre, text=caractere, command=lambda c=caractere: ajouter_caractere(c)).grid(row=ligne, column=colonne)
    colonne += 1
    if colonne > 2:
        colonne = 0
        ligne += 1

operations = "+-*/"
ligne = 1
colonne = 3
for operation in operations:
    tk.Button(fenetre, text=operation, command=lambda o=operation: ajouter_caractere(o)).grid(row=ligne, column=colonne)
    ligne += 1

# Créer les boutons spéciaux
tk.Button(fenetre, text="C", command=effacer).grid(row=4, column=0)
tk.Button(fenetre, text="=", command=calculer).grid(row=4, column=1)

# Lancer l'application
fenetre.mainloop()
