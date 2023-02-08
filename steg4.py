import os

directory = "thumbnails"

text_file_name = "nomdufichiertxt.txt"
text_content = input("Entrez le texte à enregistrer: ")


all_files = os.listdir(directory)
image_files = [f for f in all_files if f.endswith(".jpg")]
latest_image = max(image_files, key=os.path.getctime)
image_path = os.path.join(directory, latest_image)

#Exécuter la commande steghide pour cacher le fichier txt dans l'image
os.system(f"steghide embed -cf {image_path} -ef {text_file_name}")