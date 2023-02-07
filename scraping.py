import requests
from bs4 import BeautifulSoup

url = "https://www.millenium.org/guide/391312.html"

# Effectuer une demande GET sur la page web
response = requests.get(url)

# Vérifier que la requête a réussi
if response.status_code == 200:
    # Analyser le contenu de la page web avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Rechercher toutes les balises img
    images = soup.find_all("img")

    # Ouvrir un nouveau fichier texte pour stocker les URLs
    with open("image_urls.txt", "w") as file:
        # Boucle sur les images trouvées et écrire leur URL dans le fichier texte
        for image in images:
            file.write(image["src"] + "\n")

    print("Les URLs des images ont été enregistrées dans le fichier image_urls.txt")
else:
    print("La requête a échoué avec le code d'état", response.status_code)
