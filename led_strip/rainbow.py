import board
import neopixel
import time
import random
import numpy as np
from colorutils import Color

pixels = neopixel.NeoPixel(board.D18, 19)
while True:
   for t in range(19,0,-1):
        for i in range(t, t + 19):
            c = Color(hsv=((i-t) * (360/19), 1, 1))
            print("i=" + str(i))
            if(i < 19):
                pixels[i] = (c.red, c.green, c.blue)
            else:
                pixels[i - 19] = (c.red, c.green, c.blue)
pixels.show()