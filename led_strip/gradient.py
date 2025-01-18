import board
import neopixel
import sys
import time
import logging
from networktables import NetworkTables
from colorutils import Color

rchange = 0
gchange = 0
bchange = 0

def getChangeR(r, r2):
    global rchange
    rchange = (r2 - r)/19
def getChangeG(g, g2):
    global gchange
    gchange = (g2 - g)/19
def getChangeB(b, b2):
    global bchange
    bchange = (b2 -b)/19
def gradient(r, g, b, r2, g2, b2):
    global rchange
    global gchange
    global bchange

    getChangeR(r, r2)
    getChangeG(g, g2)
    getChangeB(b, b2)
    
    while r <= 255 and g <= 255 and b<=255:
        for i in range(19):
            pixels = neopixel.NeoPixel(board.D18, 19)
            pixels.fill((r, g, b))
            time.sleep(0.1)
            pixels.fill((r, g, b))
            time.sleep(0.1)
            r += rchange
            g += gchange
            b += bchange
#gradient(0, 0, 255, 0, 255, 0)