import tesserocr as ts
from PIL import Image

img = Image.open("./test2.jpg")
print(ts.image_to_text(img)) #成功识别7364