import os
import subprocess
import shutil

def embed_text_in_image():
    # Chercher le dernier dossier créé
    dir_list = sorted(os.listdir(), key=lambda x: os.path.getmtime(x))
    latest_dir = dir_list[-1]
    
    # Chercher la dernière photo dans ce dossier
    image_list = [f for f in os.listdir(latest_dir) if f.endswith('.jpg')]
    latest_image = image_list[-1]
    
    # Créer un fichier txt avec un nom logique
    text_file = latest_image.split('.jpg')[0] + '.txt'
    with open(text_file, 'w') as f:
        f.write("")
    
    # Transférer les fichiers au même niveau que le script Python
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(latest_dir, latest_image)
    text_path = os.path.join(latest_dir, text_file)
    shutil.copy(image_path, script_dir)
    shutil.copy(text_path, script_dir)
    
    # Exécuter la commande `steghide`
    image_file = os.path.basename(image_path)
    subprocess.run(["steghide", "embed", "-cf", image_file, "-ef", text_file])
    
    # Supprimer le fichier txt
    os.remove(text_file)

if __name__ == "__main__":
    embed_text_in_image()
