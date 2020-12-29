class Curtains1:
    def __init__(self, col1, col2, cT, p):
        self.panel = p
        self.colors = [col1, col2]
        self.curCol = 0
        self.startPos = 0
        self.closeTime = cT * 1000
        self.stamp = p.getMillis()
        self.closeing = True
    
    def incr(self):
        self.startPos += 1
        if (self.startPos > self.panel.width / 2):
            self.startPos = 0
            self.curCol += 1
            if (self.curCol >= len(self.colors)):
                self.curCol = 0
    
    def reset(self):
        self.curCol = 0
        self.startPos = 0
        self.stamp = self.panel.getMillis()
        self.incrAmt = 1
        
    def update(self):
        for x in range(self.startPos):
            for y in range(self.panel.height):
                self.panel.setPixel(x,y,self.colors[self.curCol])
                self.panel.setPixel(self.panel.width - x - 1,y,self.colors[self.curCol])
        lineRate = self.closeTime / (self.panel.width/ 2.0)
        if (self.panel.getMillis() - self.stamp > lineRate):
            self.stamp = self.panel.getMillis()
            self.incr()
        
class Curtains2:
    def __init__(self, col1, col2, cT, p):
        self.panel = p
        self.colors = [col1, col2]
        self.curCol = 0
        self.startPos = 0
        self.closeTime = cT * 1000
        self.stamp = p.getMillis()
        self.incrAmt = 1
        
    def incrColor(self):
        self.curCol += 1
        if (self.curCol >= len(self.colors)):
            self.curCol = 0
            
    def incr(self):
        self.startPos += self.incrAmt
        if (self.startPos > self.panel.width / 2):
            #self.incrColor()
            self.incrAmt *= -1
        if (self.startPos < 0):
            #self.incrColor()
            self.incrAmt *= -1
    
    def reset(self):
        self.curCol = 0
        self.startPos = 0
        self.stamp = self.panel.getMillis()
        self.incrAmt = 1

    def update(self):
        self.panel.setBackground((0,0,0))
        for x in range(self.startPos):
            for y in range(self.panel.height):
                self.panel.setPixel(x,y,self.colors[self.curCol])
                self.panel.setPixel(self.panel.width - x - 1,y,self.colors[self.curCol])
                
        lineRate = self.closeTime / (self.panel.width/ 2.0)
        if (self.panel.getMillis() - self.stamp > lineRate):
            self.stamp = self.panel.getMillis()
            self.incr()
        
        
