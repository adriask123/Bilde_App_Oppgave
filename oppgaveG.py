from PIL import Image, ImageOps
import pilgram

image_path = input("skriv inn navnet på bilde") 
im = Image.open(image_path)
im2 = Image.open("polaroid-frame-PNG-5.png")
im2.thumbnail((760, 760))
im = im.resize((630, 720))
im.paste(im2, (0, 0), mask=im2)

pilgram.moon(im).save("Image-Edit.jpg")
print("bilde er klart")