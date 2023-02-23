import os
import time

def main():
    image_file = input("Enter the name of the image file: ")
    cmd = "steghide extract -sf {}".format(image_file)
    os.system(cmd)
    file_path = os.path.abspath("message.txt")
    print("The hidden message was extracted to '{}'.\n".format(file_path))
    with open(file_path, "r") as f:
        print(f.read())
    time.sleep(19)
    os.remove(file_path)
    print("The hidden message was deleted.")
    
if __name__ == "__main__":
    main()
