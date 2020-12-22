import time

class SceneManager:
    def __init__(self):
        self.scenes = []
        self.index = 0
        self.stamp = self.getMillis() 

    def update(self):
        scene = self.scenes[self.index]
        scene.update()

        if (self.getMillis() - self.stamp > self.scenes[self.index].seconds * 1000):
            self.nextScene()

    def nextScene(self):
        self.index += 1
        self.stamp = self.getMillis()
        if (self.index >= len(self.scenes)):
            self.index = 0
        self.scenes[self.index].animationStarted() 
    def addScene(self, s):
        self.scenes.append(s)

    def getMillis(self):
        return int(round(time.time() * 1000))
