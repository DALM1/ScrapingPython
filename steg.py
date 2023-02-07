import os
import requests
import subprocess

current_dir = os.getcwd()

with open("image_urls.txt", "r") as f:
    url = f.read().strip()

response = requests.get(url)

image_path = os.path.join(current_dir, "image.jpg")

with open(image_path, "wb") as f:
    f.write(response.content)

subprocess.run(["steghide", "extract", "-sf", image_path])
