import os
import subprocess

def extract_hidden_file(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]
    last_image = max(image_files, key=os.path.getctime)
    subprocess.call(["steghide", "extract", "-sf", last_image])
    with open(last_image[:-4]+".txt", "r") as f:
        print(f.read())
    os.remove(last_image[:-4]+".txt")

folder_path = "/path/to/folder"
extract_hidden_file(folder_path)
