import os
import subprocess

def extract_hidden_file(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg"):
                image_file = os.path.join(root, file)
                try:
                    subprocess.run(["steghide", "extract", "-sf", image_file], capture_output=True, text=True, check=True)
                    with open("message.txt", "r") as f:
                        print(f.read())
                    os.remove("message.txt")
                except subprocess.CalledProcessError as e:
                    print(e.stderr)

folder_path = "/path/to/folder"
extract_hidden_file(folder_path)
