from Panel import Panel
from Square import Square
from Square import BouncingSquares
import time
import random
from Disperse import Disperse
from Scene import Scene
from SceneManager import SceneManager
from ImgSizer import ImgSizer


p = Panel()
sceneManager = SceneManager()
sceneManager.addScene(Scene(BouncingSquares(1,1,400,p), 300))

stamp = p.getMillis()
fRate = 60.0
while True:
    if (p.getMillis() - stamp > (1/fRate) * 1000):
        sceneManager.update()
        p.show()
        stamp = p.getMillis()
