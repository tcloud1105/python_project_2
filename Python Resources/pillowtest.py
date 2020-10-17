# pillow is the imagery processing tool

import requests
from PIL import Image
from io import BytesIO

r = requests.get("http://wallpapercave.com/wp/TuVhQdr.jpg")
print("status code ", r.status_code)

image = Image.open(BytesIO(r.content))

path = './image.jpg'
print(image.size, image.format, image.mode)
path ='./image'+image.format
try:
    image.save(path, image.format)
except IOError:
    print("cant save image")