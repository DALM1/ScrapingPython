import os

directory = "thumbnails"

#Créer un fichier text dans le dossier thumbnails
def create_text_file(text_file_name, text_content):
  text_file_path = os.path.join(directory, text_file_name)
  with open(text_file_path, "w") as text_file:
    text_file.write(text_content)

#Enregistrer du texte dans le fichier txt
text_file_name = "nomdufichiertxt.txt"
text_content = input("Entrez le texte à enregistrer: ")
create_text_file(text_file_name, text_content)

#Obtenir le nom de la dernière image dans le dossier thumbnails
all_files = os.listdir(directory)
image_files = [f for f in all_files if f.endswith(".jpg")]
latest_image = max(image_files, key=os.path.getctime)
image_path = os.path.join(directory, latest_image)

#Exécuter la commande steghide pour cacher le fichier txt dans l'image
os.system(f"steghide embed -cf {image_path} -ef {text_file_name}")
