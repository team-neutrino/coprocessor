import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 19)


while True:
    pixels.fill((0,128,128))
    time.sleep(0.5)
    pixels.fill((0,0,0))
    time.sleep(0.5)
    
    

pixels.show()

