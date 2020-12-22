from Panel import Panel
from Square import Square
from Square import BouncingSquares
import time
import random
from Disperse import Disperse
from Scene import Scene
from SceneManager import SceneManager
from ImgSizer import ImgSizer
from SinWave import SinWave


p = Panel()
sceneManager = SceneManager()
#sceneManager.addScene(Scene(ImgSizer("LIKEWILDEBLACK.png", p),  5))
#sceneManager.addScene(Scene(Disperse(10,p), 14, True))
#sceneManager.addScene(Scene(ImgSizer("Mario.png", p), 8))
#sceneManager.addScene(Scene(Disperse(10,p), 14, True))
sceneManager.addScene(Scene(SinWave(p), 20))
#sceneManager.addScene(Scene(BouncingSquares(4,4,10,p), 10))
#sceneManager.addScene(Scene(BouncingSquares(3,3,20,p), 10))
#sceneManager.addScene(Scene(BouncingSquares(1,1,300,p), 10))


stamp = p.getMillis()
fRate = 60.0
while True:
    if (p.getMillis() - stamp > (1/fRate) * 1000):
        sceneManager.update()
        p.show()
        stamp = p.getMillis()
