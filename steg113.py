import subprocess
import os

def extract_hidden_file(image_file):
    output = subprocess.run(["steghide", "extract", "-sf", image_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if output.returncode == 0:
        with open("hidden.txt", "rb") as f:
            content = f.read()
            print(content.decode("utf-8"))
    else:
        print("An error occurred: ", output.stderr)

def delete_hidden_file():
    try:
        os.remove("hidden.txt")
        print("hidden.txt file has been successfully deleted")
    except FileNotFoundError:
        print("hidden.txt file does not exist")

def main():
    image_file = input("Enter the name of the image file: ")
    extract_hidden_file(image_file)
    delete_hidden_file()

if __name__ == "__main__":
    main()
