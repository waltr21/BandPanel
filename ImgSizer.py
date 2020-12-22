from PIL import Image
from Panel import Panel
import sys

class ImgSizer:
    def __init__(self, img, p):
        self.panelRef = p

        image = Image.open(img)
        image = image.resize((42,35))

        self.pixels = image.load() # this is not a list, nor is it list()'able
        self.width, self.height = image.size

    def update(self):
        all_pixels = []
        for x in range(self.width):
            for y in range(self.height):
                cpixel = self.pixels[x, y]
                all_pixels.append(cpixel)
        count = 0
        for i in range(self.width):
            for j in range(self.height):
                self.panelRef.setPixel(i,j,all_pixels[count],0.2)
                count += 1


