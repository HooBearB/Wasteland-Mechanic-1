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
#Vehicle menus and handling can be found in VehicleHandler.py
import VehicleHandler as vehicle
#Inventory handling and management is stored in InventoryHandler.py
import InventoryHandler as inv
#Functions for loading, saving, and handling JSON files can be found in JSONHandler.py
import JSONHandler as jason
import random
import json
import os
import time

def init():
	global items
	global vehicles
	global dialogue
	global locations
	global scenarios

	time.sleep(1)
  	#Displays the logo of the MOOSE engine
	moose.displayLogo()
	time.sleep(1)
	#Opens loading loop that pulls and reads JSON files, as well as printing the loading screen animation
	x = 0
	files = [r'items', r'vehicles', r'media', r'locations', r'scenarios']
	fileData = []
	while x < len(files):
		print(moose.format.clear)
		fileData.append(jason.openFile(files[x]))
		animations.loading(x * 2, top = "Loading game...")
		time.sleep(0.2)
		x = x + 1
	items = fileData[0]
	vehicles = fileData[1]
	dialogue = fileData[2]
	locations = fileData[3]
	scenarios = fileData[4]
	print(moose.format.clear)
	animations.loading(10, top = "Loading game...")
	time.sleep(0.5)
	print(moose.format.clear)
	time.sleep(1)
	#Plays the main menu animation
	animations.mainMenu()
	decision = moose.askOption("Main Menu", ["Start game", "Load game", "Settings"])
	if decision == 1:
		print(moose.format.clear)
		startGame()
	if decision == 2:
		print(moose.format.clear)
		openGame()
	if decision == 3:
		settings()

def startGame():
	global gameData
	global gameTime
	global character
	global currentCar

	scenarioDisp = []
	scenarioList = scenarios["usable"]
	x = 0
	while x < len(scenarioList):
		scenarioDisp.append(scenarios[scenarioList[x]]["name"])
		x = x + 1
	decision = moose.askOption("Choose a scenario:", scenarioDisp)
	chosenScenario = scenarioList[decision - 1]
	loadedScenario = scenarios[chosenScenario]
	print(moose.format.clear)
	moose.scrollingText(moose.format.bold + loadedScenario["name"] + moose.format.end)
	time.sleep(0.5)
	x = 0
	while x < len(loadedScenario["description"]):
		moose.scrollingText(loadedScenario["description"][x])
		time.sleep(0.75)
		x = x + 1
	time.sleep(0.5)
	print()
	print("   Start date: " + str(loadedScenario["month"]) + "/" + str(loadedScenario["day"]) + "/" + str(loadedScenario["year"]))
	print("  Trip length: " + str(loadedScenario["journeylength"]))
	time.sleep(0.5)
	decision = moose.askOption("", ["Start game", "Back to scenario selection"])
	if decision == 1:
		try:
			direct = loadedScenario["director"]
		except:
			direct = "choice"
		try:
			scenCar = loadedScenario["vehicle"]
		except:
			scenCar = "cav_alm1"
		try:
			foodrate = loadedScenario["food"]
		except:
			foodrate = 1
		try:
			waterrate = loadedScenario["water"]
		except:
			waterrate = 1
		try:
			twinkierate = loadedScenario["twinkies"]
		except:
			twinkierate = 1
		try:
			radchange = loadedScenario["rad_change"]
		except:
			radchange = 1
		try:
			banditchange = loadedScenario["bandits"]
		except:
			banditchange = 1

		class gameData:
			director = direct
			food = 1 * foodrate
			water = 1 * waterrate
			twinkies = 1 * twinkierate
			radiation = 1 * radchange
			bandits = 1 * banditchange
			end = loadedScenario["journeylength"]
		class gameTime:
			month = loadedScenario["month"]
			day = loadedScenario["day"]
			year = loadedScenario["year"]
		class character:
			hunger = 100
			thirst = 100
			health = 100
		currentCar = vehicle.loadCar(scenCar, vehicles, items)
		vehicle.displayVehicle(currentCar, items)
		gameLoop()
	if decision == 2:
		print(moose.format.clear)
		startGame()

def gameLoop():
	global map
	
	position = 0
	map = maps.startGen(gameData.end)
	while position < gameData.end:
		print(moose.format.clear)
		map = maps.revealGen(map, position, maps.director(gameData.director, inv.determineNeeds(character.hunger, character.thirst, character.health), 5, locations["list"], locations))
		displayMap = maps.formatMap(map, position, locations)
		moose.scrollingText(displayMap[position:position + 20])
		decision = moose.askOption(str(gameTime.month) + "/" + str(gameTime.day) + "/" + str(gameTime.year), ["Start driving"])



init()