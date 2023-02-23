import os
import time

def main():
    image_file = input("Enter the name of the image file: ")
    cmd = "steghide extract -sf {}".format(image_file)
    os.system(cmd)
    text_file = os.path.splitext(image_file)[0] + ".txt"
    print("The hidden message was extracted to '{}'.".format(text_file))
    with open(text_file, "r") as f:
        print(f.read())
    time.sleep(19)
    os.remove(text_file)
    print("The hidden message was deleted.")

if __name__ == "__main__":
    main()
