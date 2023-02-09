import subprocess

def extract_hidden_file(image_file):
    passphrase = input("Enter passphrase: ")
    try:
        output = subprocess.run(["steghide", "extract", "-sf", image_file, "-p", passphrase], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
        print(output.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred: ", e.stderr)

def main():
    image_file = input("Enter the name of the image file: ")
    extract_hidden_file(image_file)

if __name__ == "__main__":
    main()
