import subprocess

def embed_text_in_image():
    print("Enter the name of the image file:")
    image_file = input().strip()
    print("Enter the name of the text file:")
    text_file = input().strip()
    subprocess.run(["steghide", "embed", "-cf", image_file, "-ef", text_file])

if __name__ == "__main__":
    embed_text_in_image()
