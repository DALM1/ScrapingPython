import os

def get_latest_file(folder):
    files = os.listdir(folder)
    paths = [os.path.join(folder, basename) for basename in files]
    return max(paths, key=os.path.getctime)

def embed_text_in_image(folder):
    latest_image = get_latest_file(folder)
    latest_image_name = os.path.basename(latest_image)
    latest_image_ext = os.path.splitext(latest_image_name)[1]
    if latest_image_ext != '.jpg':
        raise Exception("The latest file is not a jpg image")
    
    latest_txt = get_latest_file(folder)
    latest_txt_name = os.path.basename(latest_txt)
    latest_txt_ext = os.path.splitext(latest_txt_name)[1]
    if latest_txt_ext != '.txt':
        raise Exception("The latest file is not a txt file")
    
    os.system(f'steghide embed -cf {latest_image_name} -ef {latest_txt_name}')
    print(f"Text successfully embedded in {latest_image_name}")

if __name__ == '__main__':
    folder = 'thumbnails'
    embed_text_in_image(folder)
