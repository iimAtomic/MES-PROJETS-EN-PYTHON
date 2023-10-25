import tkinter as tk

def valider_inscription():
    pseudo = entry_pseudo.get()
    mdp = entry_mdp.get()
    email = entry_email.get()
    print("Inscription validée avec succès !")
    print("Pseudo"+pseudo)
    print("Mot de passe :"+ mdp)
    print("E-mail :"+email)
fenetre = tk.Tk()
fenetre.title("Inscription")
fenetre.geometry("400x400")


label_pseudo = tk.Label(fenetre, text="Pseudo :")
label_pseudo.pack()
entry_pseudo = tk.Entry(fenetre)
entry_pseudo.pack()

label_mdp = tk.Label(fenetre, text="Mot de passe :")
label_mdp.pack()
entry_mdp = tk.Entry(fenetre)  
entry_mdp.pack()

label_email = tk.Label(fenetre, text="E-mail :")
label_email.pack()
entry_email = tk.Entry(fenetre)
entry_email.pack()


btn_validation = tk.Button(fenetre, text="Valider", command=valider_inscription)
btn_validation.pack()


fenetre.mainloop()
