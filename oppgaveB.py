from PIL import Image 
import pilgram

image = input("skriv inn navnet på bilde")
im = Image.open(image)
pilgram.inkwell(im).save("Image-Edit-Inkwell.jpg")
print("bildet er klart")