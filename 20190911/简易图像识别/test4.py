import tesserocr as ts
from PIL import Image

img = Image.open("./CheckCode.png")
print(ts.image_to_text(img)) #无法识别