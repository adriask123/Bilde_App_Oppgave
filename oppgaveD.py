from PIL import Image 
import pilgram
import subprocess

image = input("skriv inn navnet på bilde") 
im = Image.open(image)

new_image = im.resize((1080, 1080))
new_image.save("image-edit.jpg")
print("bilde er klart")
valg = int(input("skriv 1 for å gå tilbake til menyen"))
if valg == 1:
    
 subprocess.run(["python", "oppgaveH.py"])