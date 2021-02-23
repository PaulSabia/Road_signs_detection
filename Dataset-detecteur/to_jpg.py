import os
from PIL import Image

folder = 'train'

path = os.path.join(os.getcwd(), folder)
images = os.listdir(path)

for img in images:
    im = Image.open(path+ '\\' +img)
    filename = os.path.basename(path+ '\\' +img)
    filename = filename.split('.')[0]
    im.save(f"{folder}/{filename}.jpg")
