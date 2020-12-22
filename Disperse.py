from Panel import Panel
import random

class Disperse:
    def __init__(self, speed, p):
        self.coords = []
        self.panelRef = p
        #self.setBackground()
        self.speed = speed
        #self.panelRef.setBackground((69,69,69))
    
    def setBackground(self):
        #self.panelRef.setBackground((69,69,69))
        for x in range(self.panelRef.width):
            for y in range(self.panelRef.height):
                self.coords.append((x,y))
    
    def reset(self):
        self.coords = []
        self.setBackground()

    def update(self):
        for t in range(self.speed):
            if (len(self.coords) == 0):
                self.setBackground()
            else:
                i = random.randint(0, len(self.coords)-1)
                temp = self.coords[i]
                self.panelRef.setPixel(temp[0], temp[1], (0,0,0))
                self.coords.remove(temp)

