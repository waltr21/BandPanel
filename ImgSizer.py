from PIL import Image

image = Image.open('nyancat_2.jpg')

pixels = image.load() # this is not a list, nor is it list()'able
width, height = image.size

all_pixels = []
for x in range(width):
    for y in range(height):
        cpixel = pixels[x, y]
        all_pixels.append(cpixel)

print(all_pixels)
#new_image = image.resize((42, 35))
#new_image.save('nyancat_2.jpg')
