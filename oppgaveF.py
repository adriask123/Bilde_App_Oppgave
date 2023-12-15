from PIL import Image, ImageOps
import pilgram 
from PIL import ImageDraw
from PIL import ImageFont

image_path = input("skriv inn navnet på bilde") 
im = Image.open(image_path)
I1 = ImageDraw.Draw(im)
myFont = ImageFont.truetype("calibri-bold.ttf", float(input("skriv inn skrift størelse her")))
I1.text((120, 0), input("skriv tekst her"), font=myFont, fill=(25, 0, 0))
im.save("edit.jpg")
print("bilde er klart")