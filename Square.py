import random

class Square:
    def __init__(self, w, h, c, p):
        # Top left x/y coordinates of the square.
        self.x = 0
        self.y = 0

        # Dimensions of the square
        self.width = w
        self.height = h

        # Reference to the panel object
        self.panel = p

        # Color of square
        self.col = c

        # Movement
        self.velocity = (random.uniform(1.0,2.0), random.uniform(1.0,2.0))

        #self.brightness = random.random()
        self.brightness = 0.9
        self.bAdjust = 0.01

    def update(self):
        # Move by x and y from velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        #self.brightness += self.bAdjust
        self.bound()



    def bound(self):
        if (self.x < 0):
            self.x = 0
            self.velocity = (self.velocity[0] * -1, self.velocity[1])
        if (self.x + self.width > self.panel.width - 1):
            self.x = self.panel.width - self.width
            self.velocity = (self.velocity[0] * -1, self.velocity[1])
        if (self.y < 0):
            self.y = 0
            self.velocity = (self.velocity[0], self.velocity[1] * -1)
        if (self.y + self.height > self.panel.height - 1):
            self.y = self.panel.height - self.height
            self.velocity = (self.velocity[0], self.velocity[1] * -1)
        if (self.brightness < 0):
            self.brightness = 0
            self.bAdjust *= -1
        if (self.brightness > 1.0):
            self.brightness = 1.0
            self.bAdjust *= -1

    def show(self):
        roundX = round(self.x)
        roundY = round(self.y)
        for curX in range(roundX, roundX + self.width):
            for curY in range(roundY, roundY + self.height):
                self.panel.setPixel(curX, curY, self.col, self.brightness)
