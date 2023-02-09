import subprocess

def extract_hidden_file(image_file):
    output = subprocess.run(["steghide", "extract", "-sf", image_file], 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            encoding="utf-8",
                            input="passphrase\n")
    if "extracted" in output.stdout:
        print(output.stdout)
        subprocess.run(["rm", "message.txt"])
    else:
        print("An error occurred: ", output.stderr)

def main():
    image_file = input("Enter the name of the image file: ")
    extract_hidden_file(image_file)

if __name__ == "__main__":
    main()
