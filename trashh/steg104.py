import os
import subprocess

def extract_hidden_file(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]
    for image_file in image_files:
        try:
            output = subprocess.run(["steghide", "extract", "-sf", image_file], capture_output=True)
            if "extracted" in str(output.stdout):
                print(f"Hidden file extracted from {image_file}")
                hidden_file = [f for f in os.listdir(folder_path) if f.endswith(".txt")][0]
                with open(hidden_file, "r") as file:
                    print(file.read())
                os.remove(hidden_file)
                break
        except Exception as e:
            print(f"Error extracting hidden file from {image_file}: {e}")

folder_path = "/path/to/folder"
extract_hidden_file(folder_path)
