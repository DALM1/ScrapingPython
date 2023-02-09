import subprocess
import os

def extract_hidden_file(image_file):
    output = subprocess.run(["steghide", "extract", "-sf", image_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if "wrote" in output.stderr:
        hidden_file = output.stderr.split("'")[1]
        with open(hidden_file, "r") as f:
            contents = f.read()
            print(contents)
    else:
        print("An error occurred: ", output.stderr)

def main():
    image_file = input("Enter the name of the image file: ")
    extract_hidden_file(image_file)
    hidden_file = image_file.split(".")[0] + ".txt"
    os.remove(hidden_file)

if __name__ == "__main__":
    main()
