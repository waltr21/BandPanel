from PIL import Image
from PIL import GifImagePlugin

class GifPlayer:
    def __init__(self, fileName, p):
        self.panel = p
        self.fileName = fileName
        self.gif = Image.open(fileName)#.convert("RGB")
        #self.gif = self.gif.resize((42,35))
        self.image = None
        self.imgIndex = 0
        self.curIndex = self.imgIndex
        self.playBackSpeed = 1
        self.nFrames = self.getNumFrames()
        self.allFrames = []
        
        self.setData()

    def setData(self):
        for i in range(0,self.nFrames):
            self.gif.seek(i)
            temp = self.gif.convert("RGB")
            pixels = temp.getdata()
            temp = temp.resize((42,35))
            self.width, self.height = temp.size
            all_pixels = []
            c = 0
            for x in range(self.width):
                for y in range(self.height):    
                    cpixel = temp.getpixel((x,y))
                    all_pixels.append(cpixel)
                    c += 1
            self.allFrames.append(all_pixels)
    
    def getNumFrames(self):
        nFrames = 0
        index = 0
        self.gif = Image.open(self.fileName)
        try:
            while True:
                self.gif.seek(index)
                index += 1
                nFrames = index
        except:
            return nFrames
            

    def incr(self):
        self.imgIndex += 1
        if(self.imgIndex >= self.nFrames):
            self.imgIndex = 0

    def update(self):
        if (self.curIndex != self.imgIndex):
            self.curIndex = self.imgIndex
            count = 0
            for i in range(self.width):
                for j in range(self.height):
                    #print(self.all_pixels[count])
                    self.panel.setPixel(i,j,self.allFrames[self.imgIndex][count],1.0)
                    count += 1
        self.incr()
        

