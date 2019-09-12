import tesserocr as ts
from PIL import Image

img = Image.open("./test1.png")
print(ts.image_to_text(img)) #成功识别