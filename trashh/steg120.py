import os
import time
import sys
import subprocess

def extract_hidden_file(image_file, passphrase):
    cmd = f"steghide extract -sf {image_file} -p {passphrase}"
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    return output.stdout

def read_hidden_file(hidden_file):
    with open(hidden_file, "r") as f:
        return f.read()

def remove_hidden_file(hidden_file):
    os.remove(hidden_file)

def empty_trash():
    trash_folder = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Windows\\INetCache")
    for root, dirs, files in os.walk(trash_folder):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            os.rmdir(os.path.join(root, d))

def main():
    image_file = input("Enter the name of the image file: ")
    passphrase = input("Enter passphrase: ")
    hidden_file = "message.txt"
    hidden_content = extract_hidden_file(image_file, passphrase)

    if "wrote extracted data to" in hidden_content:
        hidden_content = read_hidden_file(hidden_file)
        print(hidden_content)
        time.sleep(120)
        remove_hidden_file(hidden_file)
        empty_trash()
        print("Hidden file and trash successfully removed.")
    else:
        print("No hidden content found.")

if __name__ == "__main__":
    main()
