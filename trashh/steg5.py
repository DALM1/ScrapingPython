import thumbnails
import requests
import os


image_files = [f for f in all_files if f.endswith(".jpg")]
latest_image = max(image_files, key=os.path.getctime)
image_path = os.path.join(directory, latest_image)

os.system(f"steghide embed -cf {image_path} -ef {text_file_name}")
