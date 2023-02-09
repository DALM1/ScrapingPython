import os
import time

def extract_hidden_file(image_file):
    cmd = "steghide extract -sf " + image_file
    os.system(cmd)

def main():
    image_file = input("Enter the name of the image file: ")
    extract_hidden_file(image_file)
    hidden_content_file = image_file.split(".")[0] + ".txt"
    if os.path.exists(hidden_content_file):
        with open(hidden_content_file, "r") as f:
            print(f.read())
        time.sleep(120)
        os.remove(hidden_content_file)
        print("The hidden content file has been deleted.")
    else:
        print("No hidden content found.")

if __name__ == "__main__":
    main()
