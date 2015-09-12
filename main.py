import time
import sys

from grovepi import *
from grove_rgb_lcd import *

#import tabletteChecker
#import tometteChecker
import autoChecker

def printScreen(msg, R, G, B):
    # Test screen to avoid screen blinking
    global screenText
    if screenText != msg:
        screenText = msg
        setText(msg)
        setRGB(R, G, B)

def printTest(statusCode, msg):
    if statusCode:
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

# Devices ports and modes
button 		= 7			
pinMode(button,"INPUT")		
potentiometer	= 0
pinMode(potentiometer, "INPUT")

# Check if all is ok
(statusCode, msg) = autoChecker.test()
if statusCode == 1:
    printScreen("Everything is OK\nPress button...", 0, 128, 0)
    waitForButton()
else:
    printScreen("KO: " + msg, 128, 0, 0)
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
            #(statusCode, msg) = tabletteChecker.test()
            #printTest(statusCode, msg)
            #waitForButton()
        elif testMode == TOMETTE_MODE:
            printScreen("Tomette checking...", 128, 128, 128)
            #(statusCode, msg) = tometteChecker.test()
            #printTest(statusCode, msg)
            #waitForButton()
