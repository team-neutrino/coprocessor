#!/usr/bin/env python3
#
# This is a NetworkTables client (eg, the DriverStation/coprocessor side).
# You need to tell it the IP address of the NetworkTables server (the
# robot or simulator).
#
# This shows how to use a listener to listen for changes in NetworkTables
# values. This will print out any changes detected on the SmartDashboard
# table.
#

import sys
import time
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging

'''import importlib
importlib.import_module("/home/pi/Raspberry_Pi_Installer_Scripts/rpi_rgb_led_matrix/bindings/python/samples/gif_viewer")
'''

import sys
sys.path.insert(0, '/home/pi/Raspberry_Pi_Installer_Scripts/rpi_rgb_led_matrix/bindings/python/samples')
import image_viewer

logging.basicConfig(level=logging.DEBUG)

'''
if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    ip = sys.argv[1]
'''

ip = "10.39.28.2"

NetworkTables.setDashboardMode(1735)
NetworkTables.initialize(server=ip)
image = None
matrix = None
options = None



def valueChanged(table, key, value, isNew):
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))
    image_viewer.image_player("/home/pi/Downloads/trino2.jpg", image, options, matrix)
    print(matrix)




def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)


NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

# the robot needs to publish "/Intake/beam_break"
intake = NetworkTables.getTable("/Intake")
bb = intake.getAutoUpdateValue("beam_break", 0)
bb.addListener(valueChanged, NetworkTables.NotifyFlags.UPDATE)

while True:
    image_viewer.image_player("/home/pi/Downloads/trino2.jpg")
    time.sleep(1)