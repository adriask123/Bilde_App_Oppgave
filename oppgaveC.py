from PIL import Image 


image_path = input("skriv inn navnet på bilde")
im = Image.open(image_path)
image_rotate = input("skriv 90 eller 180 for å rotere")
if image_rotate == "90":
    transposed = im.transpose(Image.ROTATE_90)
elif image_rotate == "180":
   rotated = im.rotate(180)
im.save("image-edit.jpg")




