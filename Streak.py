import random
class Streak:
    def __init__(self,p):
        self.panel = p
        self.width = random.randint(2, 10)
        self.height = random.randint(1, 3)
        self.x = random.randint(0, self.panel.width)
        self.y = random.randint(0, self.panel.height)
        self.velocity = (random.uniform(1.0,2.0),0)
        self.col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        
    def bound(self):
        if (self.x > self.panel.width):
            self.x = self.width * -1
        
    
    def update(self):
        roundX = int(self.x)
        roundY = int(self.y)
        for curX in range(roundX, roundX + self.width):
            for curY in range(roundY, roundY + self.height):
                self.panel.setPixel(curX, curY, self.col)
        
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.bound()
    
class Streaks:
    def __init__(self,numStreaks, p):
        self.streaks = []
        self.panel = p
        for i in range(numStreaks):
            self.streaks.append(Streak(p))
        
    def update(self):
        self.panel.setBackground((0,0,0))
        for i in self.streaks:
            i.update()
            
        
        
        
        
