import os

def extract_text_from_image():
    image_filename = input("Enter the name of the image file: ")
    if not image_filename.endswith(".jpg"):
        raise Exception("The file is not a jpg image")
    os.system(f"steghide extract -sf {image_filename}")

if __name__ == "__main__":
    extract_text_from_image()
