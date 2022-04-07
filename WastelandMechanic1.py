"""
 ___      ___     ________     _______    ____________   ________    ___         ________    __________    ________
|\  \  __|\  \   |\   ___ \   |\   ___\  |\____   ____\ |\  _____\  |\  \       |\   ___ \  |\   ____  \  |\  ____ \
\ \  \|\ \ \  \  \ \  \__\ \  \ \  \____ \|___|\  \___| \ \ \_____  \ \  \      \ \  \__\ \ \ \  \__|\  \ \ \ \___|\\
 \ \  \ \ \ \  \  \ \   __  \  \ \____  \     \ \  \     \ \  ____\  \ \  \      \ \   __  \ \ \  \ \ \  \ \ \ \  \ \\
  \ \  \_\ \_\  \  \ \  \|\  \  \|____\  \     \ \  \     \ \ \_____  \ \  \_____ \ \  \|\  \ \ \  \ \ \  \ \ \ \__\/ \
   \ \___________\  \ \__\ \__\   |\______\     \ \__\     \ \______\  \ \_______\ \ \__\ \__\ \ \__\ \ \__\ \ \_______\
    \|___________|   \|__|\|__|   \|______|      \|__|      \|______|   \|_______|  \|__|\|__|  \|__|  \|__|  \|_______|

 ____________    ________    _______    ___  ___    ________    __________    __________   _______ 
|\   __  __  \  |\  _____\  |\  ____\  |\  \ \  \  |\   ___ \  |\   ____  \  |\___   ___\ |\  ____\
\ \  \ \ \|\  \ \ \ \____|  \ \ \___|  \ \  \_\  \ \ \  \__\ \ \ \  \__|\  \ \|__|\  \__| \ \ \___|
 \ \  \ \_\ \  \ \ \  ____\  \ \ \      \ \   __  \ \ \   __  \ \ \  \ \ \  \    \ \  \    \ \ \
  \ \  \|_|\ \  \ \ \ \___|_  \ \ \_____ \ \  \ \  \ \ \  \|\  \ \ \  \ \ \  \   _\_\  \___ \ \ \_____
   \ \__\   \ \__\ \ \______\  \ \______\ \ \__\ \__\ \ \__\ \__\ \ \__\ \ \__\ |\_________\ \ \______\
    \|__|    \|__|  \|______|   \|______|  \|__|\|__|  \|__|\|__|  \|__|  \|__| \|_________|  \|______|

 _____
/__   \
|__|\  \
   \ \  \
    \ \  \
     \ \__\
      \|__|

"""

#Made by: Flint
#Project start: April 4, 2022
#Project end: 
#Version number: v1.0.0

#A copy of MOOSE Recoded can be found in MOOSERecoded.py
import MOOSERecoded as moose
#All animations are found in GUIAnimations.py
import GUIAnimations as animations
#Map generation and calling is stored in MapHandler.py
import MapHandler as maps
#Functions for loading, saving, and handling JSON files can be found in JSONHandler.py
import JSONHandler as jason
import random
import json
import os
import time

def init():
	time.sleep(1)
  	#Displays the logo of the MOOSE engine
	moose.displayLogo()
	time.sleep(1)
	#Plays the main menu animation
	animations.mainMenu()
	moose.askOption("Main Menu", ["Start game", "Load game", "Settings"])

    
init()