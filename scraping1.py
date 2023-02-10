import requests
from bs4 import BeautifulSoup
import os

url = "https://github.com/DALM1/ScrapingPython/blob/main/scraping.py"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Rechercher toutes les balises img avec la classe "avatar"
    avatars = soup.find_all("img", {"class": "avatar"})

    # Créer un dossier pour stocker les avatars s'il n'existe pas déjà
    if not os.path.exists("avatars"):
        os.makedirs("avatars")

    # Boucle sur les avatars trouvés et les télécharger
    for avatar in avatars:
        avatar_url = avatar["src"]
        response = requests.get(avatar_url)
        if response.status_code == 200:
            with open(f"avatars/{avatar_url.split('/')[-1]}", "wb") as file:
                file.write(response.content)
else:
    print("La requête a échoué avec le code d'état", response.status_code)
