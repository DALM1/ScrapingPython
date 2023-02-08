import os
import subprocess

def embed_text_in_image():
    # Récupérer le chemin absolu du script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Récupérer le nom du dernier dossier créé
    last_folder = max([d for d in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, d))])
    # Récupérer le chemin du dernier dossier créé
    last_folder_path = os.path.join(current_dir, last_folder)
    # Récupérer le nom de la dernière photo dans le dernier dossier
    last_image = max([f for f in os.listdir(last_folder_path) if f.endswith(".jpg")], key=os.path.getctime)
    # Générer un nom de fichier pour le fichier texte
    text_file_name = last_image.split(".")[0] + ".txt"
    # Chemin absolu du fichier image
    image_path = os.path.join(last_folder_path, last_image)
    # Chemin absolu du fichier texte
    text_path = os.path.join(last_folder_path, text_file_name)
    # Copier les fichiers dans le répertoire courant
    os.rename(image_path, os.path.join(current_dir, last_image))
    os.rename(text_path, os.path.join(current_dir, text_file_name))
    # Demander à l'utilisateur d'entrer le message à cacher
    message = input("Enter the message to be hidden in the image: ")
    # Écrire le message dans le fichier texte
    with open(text_file_name, "w") as f:
        f.write(message)
    # Exécuter la commande steghide
    subprocess.run(["steghide", "embed", "-cf", last_image, "-ef", text_file_name])
    # Supprimer le fichier texte
    os.remove(text_file_name)

if __name__ == "__main__":
    embed_text_in_image()
