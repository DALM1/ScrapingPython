import os
import subprocess

def embed_text_in_image():
    all_files = []
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith(".jpg"):
                all_files.append(os.path.join(dirpath, filename))

    if not all_files:
        print("Aucune image trouvée")
        return

    last_image = max(all_files, key=os.path.getmtime)
    print(f"Dernière image trouvée : {last_image}")

    text_file_name = f"{os.path.splitext(last_image)[0]}.txt"
    with open(text_file_name, "w") as text_file:
        print("Enter the message to hide:")
        message = input().strip()
        text_file.write(message)

    subprocess.run(["steghide", "embed", "-cf", last_image, "-ef", text_file_name])
    os.remove(text_file_name)
    print(f"Message caché dans {last_image} et {text_file_name} supprimé.")

if __name__ == "__main__":
    embed_text_in_image()
