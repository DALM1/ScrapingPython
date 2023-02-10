import requests
from bs4 import BeautifulSoup

# Informations de login
payload = {
    "username": "",
    "password": ""
}

# Envoi de la requête POST pour effectuer le login
with requests.Session() as session:
    session.post("...", data=payload)
    
    # Accès à la page web protégée par login
    response = session.get("...")
    
    # Traitement du contenu HTML pour en extraire les informations souhaitées
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("src", class_="userChat")
    
    # Afficher les résultats
    for result in results:
        print(result.text)
