import time
import sys
import socket
import fcntl
import struct

from grovepi import *
from grove_rgb_lcd import *

from tabletteChecker import TabletteChecker
from tometteChecker import TometteChecker
import startupChecker

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def printScreen(msg, R, G, B):
    # Test screen to avoid screen blinking
    global screenText
    if screenText != msg:
        screenText = msg
        setText(msg)
        setRGB(R, G, B)

def printTest(statusCode, msg):
    if statusCode == 1:
        printScreen(msg, 0, 128, 0)
    else:
        printScreen(msg, 128, 0, 0)

def longButtonPress():
    global button
    buttonStatus = digitalRead(button)
    time.sleep(0.2)
    buttonStatusBis = digitalRead(button)
    return buttonStatus == 1 and buttonStatusBis == 1

def waitForButton():
    buttonStatus = longButtonPress()
    while not buttonStatus:
        buttonStatus = longButtonPress()

# Global variables
screenText = ""
testMode = None
TABLETTE_MODE = 1
TOMETTE_MODE = 2
tabletteChecker = TabletteChecker()
tometteChecker = TometteChecker()

# Devices ports and modes
button 		= 7			
pinMode(button,"INPUT")		
potentiometer	= 0
pinMode(potentiometer, "INPUT")

# Print IP
nbTry = 0
addressIP = "No IP"
try:
    addressIP = get_ip_address('wlan0')
except IOError:
    time.sleep(5)
    try:
        addressIP = get_ip_address('wlan0')
    except IOError:
        pass
printScreen(addressIP + "\nPress button...", 128, 128, 128)
waitForButton()

# Check if all is ok
(statusCode, msg) = startupChecker.test()
if statusCode == 1:
    printScreen("Everything is OK\nPress button...", 0, 128, 0)
    waitForButton()
else:
    printScreen(msg, 128, 0, 0)
    sys.exit(-1)

# Run checks
while True:
    try:
        potentValue = analogRead(potentiometer)
        if potentValue < 512:	
            printScreen("Mode tablette.\nPress button...", 0, 128, 64)
            testMode = TABLETTE_MODE
        else:
            printScreen("Mode tomette.\nPress button...", 128, 0, 64)
            testMode = TOMETTE_MODE
    except (IOError, TypeError) as e:
        print "Warning: Error reading potentiometer"
        continue

    buttonStatus = longButtonPress()
    if buttonStatus:
        if testMode == TABLETTE_MODE:
            printScreen("Tablette checking...", 128, 128, 128)
            (statusCode, msg) = tabletteChecker.test()
            printTest(statusCode, msg)
            waitForButton()
        elif testMode == TOMETTE_MODE:
            printScreen("Tomette checking...", 128, 128, 128)
            (statusCode, msg) = tometteChecker.test()
            printTest(statusCode, msg)
            waitForButton()
