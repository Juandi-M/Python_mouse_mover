# Copyright 2021, Juan Monge Jimenez, All rights reserved.

# Version 2.0 - Code optimzation and documentation.

# For pyatogui https://pyautogui.readthedocs.io/en/latest/ library.
# Please run the following command: <import pyautogui> on your cmd or terminal

from time import sleep
import time
import pyautogui


#  ---- Initial statement----
print('Program running')

# ----Pyautogui config statement----
screenSize = screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print("Your screen size is = ", screenSize)

mouseCurrentPosition = currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print ("your current mouse position is = ", mouseCurrentPosition)

pyautogui.FAILSAFE = False

# ---- Condition for intial mouse movement ---

program_starts = time.time()

while True:

    sleep (10) #Change how often the mouse moves in seconds

    #Counter for time in seconds the program has run since execution.
    now = time.time()
    print("It has been {0} seconds since mouse mover is started".format(now - program_starts))

    #actual mose movement from left to right
    pyautogui.moveTo(576, 450) # Move the mouse to XY coordinates. 
    pyautogui.moveTo(1152, 450) # Move the mouse to XY coordinates. 