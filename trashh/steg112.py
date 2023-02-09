import subprocess

def extract_hidden_file(image_file):
    output = subprocess.run(["steghide", "extract", "-sf", image_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if "wrote extracted data to" in output.stderr:
        txt_file = output.stderr.split(" ")[-1].strip()
        with open(txt_file, "r") as file:
            print(file.read())
    else:
        print("An error occurred: ", output.stderr)

def delete_txt_file(txt_file):
    output = subprocess.run(["del", txt_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if output.returncode == 0:
        print(f"The file {txt_file} was successfully deleted.")
    else:
        print("An error occurred: ", output.stderr)

def main():
    image_file = input("Enter the name of the image file: ")
    extract_hidden_file(image_file)
    txt_file = input("Enter the name of the txt file: ")
    delete_txt_file(txt_file)

if __name__ == "__main__":
    main()
