import os
import subprocess

def extract_hidden_file(image_file):
    try:
        output = subprocess.call(["steghide", "extract", "-sf", image_file])
        print(output.stdout)
        os.remove(image_file)
    except Exception as e:
        print("An error occurred: ", str(e))

def main():
    image_file = input("Enter the name of the image file: ")
    extract_hidden_file(image_file)

if __name__ == "__main__":
    main()
