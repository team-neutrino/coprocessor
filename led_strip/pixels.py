import board
import neopixel
import time
import random
from colorutils import Color
pixels = neopixel.NeoPixel (board.D18, 19)
delay = 0.05
while True:
	for t in range(19):
		for i in range(t, t + 19):
			c = Color(hsv=((i-t) * (360/19), 1, 1))
			print("i=" + str(i))
			if(i < 19):
				pixels[i] = (c.red, c.green, c.blue)
			else:
				pixels[i - 19] = (c.red, c.green, c.blue)
		time.sleep(delay)
		print("t=" + str(t))
	delay = random.uniform(0,0.5)
	for t in range(19,0,-1):
		for i in range(t, t + 19):
			c = Color(hsv=((i-t) * (360/19), 1, 1))
			print("i=" + str(i))
			if(i < 19):
				pixels[i] = (c.red, c.green, c.blue)
			else:
				pixels[i - 19] = (c.red, c.green, c.blue)
		time.sleep(delay)
		print("t=" + str(t))
	delay = random.uniform(0,0.5)
pixels.show()
