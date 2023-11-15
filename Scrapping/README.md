# Scraping sur un site web

Ce script Python effectue le scraping des avis et des noms d'appareils à partir du site [Darty](https://www.darty.com/). Les données collectées sont ensuite sauvegardées dans un fichier JSON et affichées dans un graphique à barres à l'aide de Pandas et Matplotlib.

## Prérequis

- Python 3.x
- Modules Python requis : `pandas`, `beautifulsoup4`, `requests`, `matplotlib`

Installez les modules requis avec la commande suivante :
```bash
 pip install pandas beautifulsoup4 requests matplotlib
```
Utilisation :
```bash
Clonez le dépôt :
git clone https://github.com/iimAtomic/MES-PROJETS-EN-PYTHON.git
cd ...

```
Exécutez le script :
```bash
python scrap.py
```

Le script collecte les données, les sauvegarde dans un fichier JSON nommé Information.json, et affiche un graphique à barres montrant le nombre d'avis pour chaque appareil.
Avertissement
Le scraping de sites Web peut être soumis à des restrictions et politiques d'utilisation du site. Assurez-vous de respecter ces politiques lors de l'utilisation de ce script.

Licence
Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.
