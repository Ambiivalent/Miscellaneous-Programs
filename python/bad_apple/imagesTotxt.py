import os
from PIL import Image

WIDTH = 960//10
HEIGHT = 720//10

folder = "bad_apple"
files = os.listdir(folder)
toWrite = open('data.txt', "w")
count = 0

for images in files:
    baseImage = Image.open(folder + "/" + f"{count}.jpg")
    baseImage = baseImage.resize((WIDTH, HEIGHT))
    baseImage = baseImage.convert("L")
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if baseImage.getpixel((x,y)):
                toWrite.write("1")
            else: toWrite.write("0")
        toWrite.write("\n")          
    count += 1

toWrite.close()
print("CLOSE")