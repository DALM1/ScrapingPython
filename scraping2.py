import os
import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = "https://github.com/DALM1/ScrapingPython/blob/main/scraping.py"

# Répertoire où les avatars seront enregistrés
folder = "avatars"

# Effectuer une demande GET sur la page web
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Analyser le contenu de la page web avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Rechercher toutes les balises img
    images = soup.find_all("img")

    # Si le répertoire n'existe pas, le créer
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Boucle sur les images trouvées
    for image in images:
        avatar_url = image.get("src")
        if avatar_url:
            # Vérifier que l'URL est valide
            if "http" not in avatar_url:
                # Si l'URL n'est pas valide, la préfixer avec http
                avatar_url = "http:" + avatar_url

            response = requests.get(avatar_url)

            # Vérifier que la requête a réussi
            if response.status_code == 200:
                # Déterminer le nom de fichier à enregistrer
                filename = os.path.join(folder, os.path.basename(avatar_url))

                # Écrire les données téléchargées dans un fichier
                with open(filename, "wb") as file:
                    file.write(response.content)

                print(f"L'avatar {avatar_url} a été enregistré avec succès en tant que {filename}")
            else:
                print(f"La requête pour l'avatar {avatar_url} a échoué avec le code d'état {response.status_code}")
        else:
            print(f"L'URL de l'avatar n'a pas été trouvée pour l'image {image}")
else:
    print(f"La requête a échoué avec le code d'état {response.status_code}")
