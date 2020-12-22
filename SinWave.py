import time
import math
import random


class SinWave:
    def __init__(self, p):
        self.panel = p
        self.size = self.panel.width
        self.waveHeight = 4.0
        self.speed = 0.2
        self.pixels1 = []
        self.pixels2 = []
        for i in range(self.size):
            c = i / (self.size * 1.0)
            rVal = self.lerp(0,255,c)
            bVal = self.lerp(0,255,1 - c)
            self.pixels1.append((rVal, bVal, 0))
        for i in range(self.size):
            c = i / (self.size * 1.0)
            rVal = self.lerp(0,255,c)
            bVal = self.lerp(0,255,1 - c)
            self.pixels2.append((bVal, rVal, 0))
        self.stamp = time.time()
        
    def lerp(self, a, b, c):
        return (c * a) + ((1-c) * b)
    
    def update(self):
        self.panel.setBackground((0,0,0))
        t = (time.time() - self.stamp) * self.speed
        for xVal in range(len(self.pixels1)):
            p = self.pixels1[xVal]
            yVal = round(self.panel.height / 3) + round(math.sin(xVal * t) * self.waveHeight) 
            self.panel.setPixel(xVal,yVal,p,1)
            
        for xVal in range(len(self.pixels2)):
            p = self.pixels2[xVal]
            yVal = (1 - round(self.panel.height / 3)) + round(math.sin(xVal * t) * self.waveHeight) 
            self.panel.setPixel(xVal,yVal,p,1)
        
            
