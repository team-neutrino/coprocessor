import time
import board
import neopixel

num_pixels = 13

pixels = neopixel.NeoPixel(board.D18, num_pixels)

def create_gradient(start_color, end_color, steps):
    gradient =[]
    for i in range(steps):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / steps)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / steps)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / steps)
        gradient.append((r,g,b))
    return gradient

color1 = (255, 0 ,0)
color2 = (0, 0, 255)

gradient = create_gradient(color1, color2, num_pixels)

for i in range(num_pixels):
    pixels[i] = gradient[i]
    time.sleep(0.05)