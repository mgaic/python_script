import tesserocr as ts
from PIL import Image

img = Image.open("./test3.jpg")
print(ts.image_to_text(img)) #无法识别