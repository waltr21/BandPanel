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
from ColorLerp import ColorLerp
from GifPlayer import GifPlayer

p = Panel()
sceneManager = SceneManager()
# sceneManager.addScene(Scene(ColorLerp(0.05,p), 40))
# sceneManager.addScene(Scene(Disperse(10,p), 14, True))
# sceneManager.addScene(Scene(ImgSizer("tree.png", p),  25))
# sceneManager.addScene(Scene(Disperse(10,p), 14, True))
# sceneManager.addScene(Scene(ImgSizer("RoughDong.png", p),  10))
# sceneManager.addScene(Scene(Disperse(10,p), 14, True))
# sceneManager.addScene(Scene(ImgSizer("Mario.png", p), 30))
# sceneManager.addScene(Scene(Disperse(10,p), 14, True))
# sceneManager.addScene(Scene(SinWave(p), 35))
# sceneManager.addScene(Scene(Disperse(10,p), 30, True))
# sceneManager.addScene(Scene(BouncingSquares(4,4,10,p), 30))
# sceneManager.addScene(Scene(Disperse(10,p), 14, True))
# sceneManager.addScene(Scene(BouncingSquares(3,3,20,p), 30))
# sceneManager.addScene(Scene(Disperse(10,p), 14, True))
# sceneManager.addScene(Scene(BouncingSquares(1,1,200,p), 30))
# sceneManager.addScene(Scene(Disperse(10,p), 14, True))
sceneManager.addScene(Scene(GifPlayer("karate.gif",p), 10))
sceneManager.addScene(Scene(GifPlayer("3dmario2.gif",p), 10))
sceneManager.addScene(Scene(GifPlayer("tato.gif",p), 10))



stamp = p.getMillis()
fRate = 60.0
while True:
    if (p.getMillis() - stamp > (1/fRate) * 1000):
        sceneManager.update()
        p.show()
        stamp = p.getMillis()
