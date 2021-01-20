# threesixty.py

# By Brendan Payne

# Description: 
# Connects to the Neato via USB, and commands it to spin 360 degrees.


DEVICE = '/dev/ttyACM0'

import serial
import time

robot = serial.Serial(DEVICE) # connect to serial bus on Neato

def docommand(port, command): 
	port.write((command + '\n').encode()) # sends encoded command to bot

docommand(robot, 'testmode on')

docommand(robot, 'playsound soundid 1') # plays a sound to notifiy that the script is running
time.sleep(2) # wait two seconds
docommand(robot, 'setmotor lwheeldist 200 rwheeldist 200 speed 200') # move 20cm forward
time.sleep(2) # wait two seconds
docommand(robot, 'setmotor lwheeldist 850 rwheeldist -850 speed 200') # turn 360 degrees counterclockwise 
time.sleep(5) # wait five seconds
docommand(robot, 'setmotor lwheeldist -120 rwheeldist -120 speed 100') # reverse back to hub
time.sleep(2) # wait two seconds
docommand(robot, 'playsound soundid 2') # plays sound to notify that script has finished


robot.close() # close connection with serial
