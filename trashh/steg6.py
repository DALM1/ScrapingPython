import os

# répertoire thumbnails
directory = "thumbnails"

# Récupération du nom de la dernière photo
files = os.listdir(directory)
files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)))
last_file = files[-1]

# Commande steghide
command = "steghide embed -cf " + directory + "/" + last_file + " -ef " + directory + "/message.txt"
os.system(command)
