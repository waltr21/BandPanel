from PIL import Image
from Panel import Panel

p = Panel()

image = Image.open('nyancat_2.jpg')

pixels = image.load() # this is not a list, nor is it list()'able
width, height = image.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        all_pixels.append(cpixel)
count = 0
for i in range(width):
    for j in range(height):
        p.setPixel(i,j,all_pixels[count],0.2)
        count += 1

p.show()
