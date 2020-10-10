import board
import neopixel
import time
import random

class Panel:
    def __init__(self):
        self.width = 42
        self.height = 35
        self.size = self.width * self.height
        self.grid = None
        self.initGrid()
        self.brightness = 0.05
        self.pixels = neopixel.NeoPixel(board.D18, self.size, auto_write=False)

    def initGrid(self):
        self.grid = [[0 for i in range(self.height)] for j in range(self.width)]
        pixelCount = 0
        colCount = 0
        x = self.width - 1

        while (x >= 0):
            if (colCount % 2 == 0):
                y = self.height - 1
                while (y >= 0):
                    #print("Setting: " + str(x) + ", " + str(y))
                    self.grid[x][y] = pixelCount
                    pixelCount += 1
                    y -= 1
            else:
                y = 0
                while (y < self.height):
                    self.grid[x][y] = pixelCount
                    pixelCount += 1
                    y += 1
            x -= 1
            colCount += 1

    def getColor(self, col, brightness=-1):
        b = 0
        if (brightness < 0):
            b = self.brightness
        else:
            b = brightness
        return (col[1] * b, col[0] * b, col[2] * b)

    def setBackground(self, col):
        for i in range(self.size):
            self.pixels[i] = self.getColor(col)

    def setPixel(self, x, y, col, brightness=-1):
        self.pixels[self.grid[x][y]] = self.getColor(col, brightness)

    def show(self):
        self.pixels.show()

    def getMillis(self):
        return int(round(time.time() * 1000))
