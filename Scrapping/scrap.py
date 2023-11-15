# Import des bibliothèques nécessaires
import json
import os
import tkinter as tk
import pandas as pd
from bs4 import BeautifulSoup
import requests as rq
import matplotlib.pyplot as plt

# URL de la page à analyser
url = "https://www.darty.com/"
response = rq.get(url)
html_content = response.content

# Script pour forcer la création du fichier JSON dans le dossier du projet
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "Information.json")

# Récupération du contenu HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Récupération de tous les articles
appareils = soup.find_all('article', class_='product')
data = []

# Boucle pour afficher chaque article
for appareil in appareils:
    avis_appareil = appareil.find('div', class_='reviews')
    if avis_appareil:
        nombre_avis_texte = avis_appareil.text.replace(',', '').strip().split()[0]
        nombre_avis = nombre_avis_texte
        print(f"Nombre d'avis: {nombre_avis}")

        nom_app_element = appareil.find('a', class_='name ellipsis')
        if nom_app_element:
            nom_appareil = nom_app_element.text.strip()
            print(f"Nom de l'appareil: {nom_appareil}")
            data.append({'Nom de l\'appareil': nom_appareil, 'Nombre d\'avis': nombre_avis})
            print("------")

df = pd.DataFrame(data)

# Affichage
plt.figure(figsize=(18, 12))
plt.bar(df['Nom de l\'appareil'], df['Nombre d\'avis'].astype(int))
plt.xlabel('Nom de l\'appareil')
plt.ylabel('Nombre d\'avis')
plt.title('Nombre d\'avis par appareil')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print(df)
