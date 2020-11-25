from Panel import Panel
import time
import random

p = Panel()

i = 0
while True:
    if (i < 10):
        p.setBackground((0,0,0))
        p.show()
        p.setBackground((0,100,0))
        p.show()
        i = i+1
        #time.sleep(1)

