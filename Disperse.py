from Panel import Panel
import random

class Disperse:
    def __init__(self, p):
        self.coords = []
        for x in range(p.width):
            for y in range(p.height):
                self.coords.append((x,y))
        
        self.panelRef = p
        self.panelRef.setBackground((255,0,255))
    
    def update(self):
        for t in range(5):
            i = random.randint(0, len(self.coords)-1)
            temp = self.coords[i]
            self.panelRef.setPixel(temp[0], temp[1], (0,0,0))
            self.coords.remove(temp)

