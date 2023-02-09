import os
import pexpect

def extract_hidden_file(image_file):
    cmd = "steghide extract -sf " + image_file
    try:
        result = pexpect.run(cmd)
        return result.decode("utf-8").strip()
    except Exception as e:
        print("An error occurred while extracting the hidden file:", e)
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
