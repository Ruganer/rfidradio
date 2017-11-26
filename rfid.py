# Start setting python/Rpi parimeters
import os
import time
import sys

id = "0008482812"  #This is where you configure the correct ID, current version only supports one correct ID 
scan = "0"  # presets the scan resault as 0


while(True):                                       #Begin loop
	scan = raw_input("Please scan code")
        if scan == id:                             #If scanned ID is correct, perform script
		os.system("volumio play")          #Perform action 
		print ("pin high, waiting")        #prints message to console 
		scan = "0"                         # resets the scan 
	else:                                      # if the code is wrong, this performs
		print ("wrong code")               # print message to constole 
		time.sleep(1)                      # wait a second 
