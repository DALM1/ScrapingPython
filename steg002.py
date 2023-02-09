import os
import time

def main():
    image_file = input("Enter the name of the image file: ")
    cmd = "steghide extract -sf {}".format(image_file)
    os.system(cmd)
    print("The hidden message was extracted to 'message.txt'.")
    with open("message.txt", "r") as f:
        print(f.read())
    time.sleep(19)
    os.remove("message.txt")
    print("The hidden message was deleted.")

if __name__ == "__main__":
    main()
