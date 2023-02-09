import subprocess
import os

def extract_text_from_image():
    print("Enter the name of the image file:")
    image_file = input().strip()
    
    subprocess.run(["steghide", "extract", "-sf", image_file])
    
    text_file = image_file.split(".")[0]+".txt"
    
    with open(text_file, "r") as f:
        print("The extracted text is:")
        print(f.read())
    
    os.remove(text_file)
    print("The text file has been deleted.")

if __name__ == "__main__":
    extract_text_from_image()
