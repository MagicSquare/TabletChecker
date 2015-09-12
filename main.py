from grovepi import *
from grove_rgb_lcd import *

def printScreen(msg, R, G, B):
    # Test screen to avoid screen blinking
    global screenText
    if screenText != msg:
        screenText = msg
        setText(msg)
        setRGB(R, G, B)

screenText = ""

# Devices ports and modes
button 		= 7			
pinMode(button,"INPUT")		
potentiometer	= 0
pinMode(potentiometer, "INPUT")

# Run checks
while True:
    try:
        testMode = analogRead(potentiometer)
        if testMode < 512:	
            printScreen("Mode tablette. Press button...", 0, 128, 64)
        else:
            printScreen("Mode tomette. Press button...", 128, 0, 64)
    except (IOError, TypeError) as e:
        print "Warning: Error reading potentiometer"
#	button_status= digitalRead(button)
#	print button_status

#		if button_status:	#If the Button is in HIGH position, run the program
#			digitalWrite(buzzer_pin,1)						
#			# print "\tBuzzing"			
#		else:		#If Button is in Off position, print "Off" on the screen
#			digitalWrite(buzzer_pin,0)
			# print "Off"			
#	except KeyboardInterrupt:	# Stop the buzzer before stopping
#		digitalWrite(buzzer_pin,0)
#		break
#	except (IOError,TypeError) as e:
#		print "Error"
