import os

def get_latest_file(folder_path):
    list_of_files = os.listdir(folder_path)
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file

def embed_text_in_image(text_file, folder_path):
    latest_file = get_latest_file(folder_path)
    if latest_file.endswith('.jpg'):
        command = f'steghide embed -cf {latest_file} -ef {text_file}'
        os.system(command)
        print(f'Text successfully embedded in image {latest_file}')
    else:
        raise Exception("The latest file in the folder is not a .jpg image.")

def main():
    folder_path = 'thumbnails'
    text_file = 'text.txt'
    try:
        embed_text_in_image(text_file, folder_path)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
