from PIL import Image 
import pilgram

image = input("skriv inn navnet på bilde")
im = Image.open(image)
pilgram.toaster(im).save("Image-Edit-Toaster.jpg")
print("bildet er klart")