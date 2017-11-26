#!/usr/bin/env python
#
# Raspberry Pi Rotary Test Encoder Class
#
# Author : Bob Rathbone
# Site   : http://www.bobrathbone.com
#
# This class uses a standard rotary encoder with push switch
#

import sys
import time
from rotary_class import RotaryEncoder
import subprocess

# Define GPIO inputs
PIN_A = 5
PIN_B = 6
BUTTON = 13

# This is the event callback routine to handle events
def switch_event(event):
    if event == RotaryEncoder.CLOCKWISE:
        print "Volume up"
        subprocess.call(['volumio', 'volume', 'plus'])

    elif event == RotaryEncoder.ANTICLOCKWISE:
        print "Volume down"
        subprocess.call(['volumio', 'volume', 'minus'])

    elif event == RotaryEncoder.BUTTONDOWN:
        
        print "Play"
        subprocess.call(['volumio', 'play'])
    elif event == RotaryEncoder.BUTTONDOWN:
        print "Pause"
        subprocess.call(['volumio', "pause"])

#   elif event == RotaryEncoder.BUTTONUP:
#       print "Button up"
    return

# Define the switch
rswitch = RotaryEncoder(PIN_A,PIN_B,BUTTON,switch_event)

while True:
    time.sleep(0.5)

