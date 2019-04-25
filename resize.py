import os.path
import PIL
from PIL import Image

size = 520, 520
repo = "/opt/platform/data/images"

original_folder = os.path.join(repo, 'original')
resize_folder = os.path.join(repo, 'resized')
source_files = os.listdir(original_folder)

def resize_img(filename):
    image = Image.open(os.path.join(original_folder, filename))
    image.thumbnail(size, Image.ANTIALIAS)
    image.save(os.path.join(resize_folder, filename), "JPEG")

for content in source_files:
    resize_img(content)
