import requests
from bs4 import BeautifulSoup
import os

# URL de la page à scrapper
url = "https://www.youtube.com"

# Effectuer une demande GET sur la page web
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Analyser le contenu de la page web avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Rechercher toutes les balises img
    images = soup.find_all("img")

    # Créer le dossier "images" s'il n'existe pas
    if not os.path.exists("images"):
        os.makedirs("images")

    # Boucle sur toutes les images trouvées
    for index, image in enumerate(images):
        # Récupérer l'URL de l'image
        img_url = image.get("src")

        # Effectuer une demande GET pour télécharger l'image
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            # Enregistrer l'image dans le dossier "images"
            with open(f"images/image_{index}.jpg", "wb") as file:
                file.write(img_response.content)
    print("Les images ont été téléchargées avec succès!")
else:
    print("La requête a échoué avec le code d'état", response.status_code)
