import requests
from bs4 import BeautifulSoup

# Informations de login
payload = {
    "username": "myusername",
    "password": "mypassword"
}

# Envoi de la requête POST pour effectuer le login
with requests.Session() as session:
    session.post("https://www.example.com/login", data=payload)
    
    # Accès à la page web protégée par login
    response = session.get("https://www.example.com/protected_page")
    
    # Traitement du contenu HTML pour en extraire les informations souhaitées
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("div", class_="result")
    
    # Afficher les résultats
    for result in results:
        print(result.text)
