import board
import neopixel
import sys
import time
import logging
from gradient import gradient
from networktables import NetworkTables
from colorutils import Color

logging.basicConfig(level=logging.DEBUG)

'''
if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    ip = sys.argv[1]
'''

ip = "10.39.28.2"
global currentColorRGB
currentColorRGB = [255, 0, 0]
previousColorRGB = currentColorRGB
pixels = neopixel.NeoPixel(board.D18, 19, auto_write=False)

NetworkTables.setDashboardMode(1735)
NetworkTables.initialize(server=ip)

def setCurrentColor(r, g, b):
    global currentColorRGB
    currentColorRGB[0] = r
    currentColorRGB[1] = g
    currentColorRGB[2] = b
   
def valueChanged(table, key, value, isNew):
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    global currentColorRGB
    if value == "white":
        setCurrentColor(255, 255, 255)
    if value == "red":
        setCurrentColor(255, 0, 0)
    if value == "orange":
        setCurrentColor(255, 165, 0)
    if value == "yellow":
        setCurrentColor(255, 255, 0)
    if value == "green":
        setCurrentColor(0, 255, 0)
    if value == "blue":
        setCurrentColor(0, 0, 255)
    if value =="purple":
        setCurrentColor(255, 0, 255)
    if value == "cyan":
        setCurrentColor(0, 255, 255)
    if value == "black":
        setCurrentColor(0, 0, 0)
    if value == "indigo":
        setCurrentColor(75, 0, 130)
    if value =="teal":
        setCurrentColor(0, 128, 128)
#    for i in range(1):
#        if value == "blinkwhite":
#            pixels.fill((255,255,255))
#            time.sleep(0.5)
#            pixels.fill((0,0,0))
#            time.sleep(0.5)
#        if value == "blinkteal":
#            pixels.fill((0,128,128))
#            time.sleep(0.5)
#            pixels.fill((0,0,0))
#            time.sleep(0.5)
#    for t in range(19,0,-1):
#        for i in range(t, t + 19):
#            if value == "rainbow":
#                c = Color(hsv=((i-t) * (360/19), 1, 1))
#                if(i < 19):
#                    pixels[i] = (c.red, c.green, c.blue)
#                else:
#                    pixels[i - 19] = (c.red, c.green, c.blue)
                    
        

def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)

NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)
    # the robot needs to publish "/LED/color"
led = NetworkTables.getTable("/LED")
color = led.getAutoUpdateValue("color", "")
color.addListener(valueChanged, NetworkTables.NotifyFlags.UPDATE)

while True:
    time.sleep(0.1)
    print("r %d" % currentColorRGB[0])
    print("g %d" % currentColorRGB[1])
    print("b %d" % currentColorRGB[2])
    print(" ")
    pixels.fill((currentColorRGB[0],currentColorRGB[1], currentColorRGB[2] ))
    if previousColorRGB != currentColorRGB:
        print("hi")
        gradient(previousColorRGB[0], previousColorRGB[1], previousColorRGB[2], currentColorRGB[0], currentColorRGB[1], currentColorRGB[2])
    previousColorRGB = currentColorRGB
    pixels.show()