import os
import requests
from bs4 import BeautifulSoup

# URL de la page à analyser
url = "https://soundcloud.com/dalm111/likes"

# Télécharger le contenu de la page
response = requests.get(url)

# Analyser le contenu avec BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Répertoire où enregistrer les images
directory = "thumbnails"

# Créer le répertoire s'il n'existe pas
if not os.path.exists(directory):
    os.makedirs(directory)

# Rechercher toutes les images
images = soup.find_all("img")

# Boucle sur les images trouvées
for image in images:
    # Obtenir l'URL de l'image
    image_url = image["src"]

    # Effectuer une demande GET pour télécharger l'image
    image_response = requests.get(image_url)

    # Déterminer le nom de fichier en fonction de l'URL
    filename = os.path.join(directory, image_url.split("/")[-1])

    # Enregistrer l'image dans le fichier
    with open(filename, "wb") as f:
        f.write(image_response.content)
    
    # Exécuter la commande Steghide pour extraire les données cachées
    os.system(f"steghide extract -sf {filename}")
