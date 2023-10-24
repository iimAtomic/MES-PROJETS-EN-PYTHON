'''x= 0
while x<= 10:
    if (x% 2) == 0:
        print(x)
    x+=1
else : print("je suis noob")'''


'''
for i in range(5):
    if i % 2 == 0:
        print(i)
        
 Créer un programme qui permet à l'utilisateur de saisir et 
 de gérer des informations personnelles telles que le nom, l'âge, la taille, 
 la liste des fruits préférés, un message de salutation personnalisé, les propriétés 
 d'un produit, la manipulation de chaînes de caractères et l'entrée de l'utilisateur.
'''

nom = input("Entrez un nom : ")
nom = nom.upper()
prenom = input("Entrez un prénom : ")
fruits = input("Entrez vos fruits préférés séparés par des virgules  svp :) : ")
liste_fruits = fruits.split(',')

message = "Bonjour " + nom + " " + prenom + ", je sais que vous aimez les "
message += ', '.join(liste_fruits) + "."
print(message)
