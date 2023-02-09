import subprocess
import os
import signal

def extract_hidden_file(image_file):
    cmd = "steghide extract -sf " + image_file
    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
        if result.returncode != 0:
            print("Error: ", result.stderr.decode())
        if result.returncode == 0:
            return result.stdout.decode("utf-8").strip()
        else:
            return None
    except subprocess.TimeoutExpired:
        print("Extracting hidden file timed out after 10 seconds.")
        return None

def display_hidden_content(hidden_content):
    if hidden_content is not None:
        print(hidden_content)
    else:
        print("No hidden content found.")

def delete_hidden_file(image_file):
    hidden_file = image_file.split(".")[0] + ".txt"
    if os.path.exists(hidden_file):
        os.remove(hidden_file)

def main():
    image_file = input("Enter the name of the image file: ")    
    hidden_content = extract_hidden_file(image_file)
    display_hidden_content(hidden_content)
    delete_hidden_file(image_file)

if __name__ == "__main__":
    main()
