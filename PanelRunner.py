from Panel import Panel
from Square import Square
import time
import random

p = Panel()

squares = []
for i in range(4):
    temp = Square(7,7,(255,0,0),p)
    temp.x = random.randint(0, p.width)
    temp.y = random.randint(0, p.height)
    temp.col = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    squares.append(temp)

stamp = p.getMillis()
fRate = 60.0
while True:
    if (p.getMillis() - stamp > (1/fRate) * 1000):
        p.setBackground((0,0,0))
        for square in squares:
            square.update()
            square.show()
        p.show()
        stamp = p.getMillis()
