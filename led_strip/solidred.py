import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 19)

for pixel_idx in range(19):
    pixels[pixel_idx] = (255, 0, 0)

pixels.show()


