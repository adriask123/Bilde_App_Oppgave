from PIL import Image 
import pilgram
import subprocess



image = input("skriv inn navnet på bilde")
im = Image.open(image)
pilgram.toaster(im).save("Image-Edit-Toaster.jpg")
print("bildet er klart")

valg = int(input("skriv 1 for å gå tilbake til menyen"))
if valg == 1:
    
 subprocess.run(["python", "oppgaveH.py"])