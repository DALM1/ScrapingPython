import os
import subprocess

def extract_hidden_file(folder_path):
    # Rechercher toutes les images .jpg dans le répertoire
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg"):
                image_path = os.path.join(root, file)
                
                # Extraire le fichier caché à partir de l'image
                output = subprocess.run(["steghide", "extract", "-sf", image_path], capture_output=True)
                
                # Si le fichier caché est trouvé, l'afficher dans le terminal et le supprimer
                if output.returncode == 0:
                    hidden_file = output.stdout.decode().strip().split("\n")[-1].split(" ")[-1]
                    with open(hidden_file, "r") as f:
                        print(f.read())
                    os.remove(hidden_file)

# Définir le chemin vers le répertoire où se trouve l'image
folder_path = "/path/to/folder"

# Appeler la fonction pour extraire le fichier caché
extract_hidden_file(folder_path)
