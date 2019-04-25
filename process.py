import os.path
import shlex
import subprocess
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

    if os.path.isfile(os.path.join(resize_folder, content)) is False:
        resize_img(os.path.join(resize_folder, content))

    for style in source_files:

        for alg in ["gatys", "chen-schmidt", "chen-schmidt-inverse"]:

            if os.path.isfile("{0}_{1}_{2}_ss1.0_sw5.0.png".format(content, style, alg)) is False:
                command = "nvidia-docker run --rm -v {0}:/images albarji/neural-style --content resized/{1} --style resized/{2} --alg {3}".format(repo, content, style, alg)
                print(command)
                subprocess.call(shlex.split(command))
