import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 19)

while True:
    pixels.fill((255,255,255))
    time.sleep(0.5)
    pixels.fill((0,0,0))
    time.sleep(0.5)
    
    

pixels.show()
