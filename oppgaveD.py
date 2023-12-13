from PIL import Image 
import pilgram

image = input("skriv inn navnet på bilde") 
im = Image.open(image)

new_image = im.resize((1080, 1080))
new_image.save("image-edit.jpg")