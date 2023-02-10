import requests
from bs4 import BeautifulSoup
import os

url = "https://soundcloud.com/dalm111/likes"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    images = soup.find_all("img")

    if not os.path.exists("thumbnails"):
        os.makedirs("thumbnails")

    for image in images:
        img_url = image["src"]
        if "http" not in img_url:
            # sometimes an image source is relative 
            # if it is provide the base url which also happens 
            # to be the site variable atm. 
            img_url = url + img_url
        
        response = requests.get(img_url)
        with open(f"thumbnails/{img_url.split('/')[-1]}", "wb") as file:
            file.write(response.content)
    
    print("Thumbnails downloaded successfully")
else:
    print("Request failed with status code", response.status_code)
