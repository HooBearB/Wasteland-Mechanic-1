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

# A copy of MOOSE Recoded can be found in MOOSERecoded.py
import MOOSERecoded as moose
# All animations are found in GUIAnimations.py
import GUIAnimations as animations
# Vehicle menus and handling can be found in VehicleHandler.py
import VehicleHandler as vehicle

# Other necessary modules are imported as well
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
  	# Displays the logo of the MOOSE engine
	moose.displayLogo()
	time.sleep(1)
	# Opens loading loop that pulls and reads JSON files, as well as printing the loading screen animation
	x = 0
	files = [r'items', r'vehicles', r'media', r'locations', r'scenarios']
	fileData = []
	while x < len(files):
		print(moose.format.clear)
		fileData.append(moose.jason.openFile(files[x]))
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
	# Opens and creates a list of scenarios found in the associated JSON file
	x = 0
	while x < len(scenarioList):
		scenarioDisp.append(scenarios[scenarioList[x]]["name"])
		x = x + 1
	scenarioDisp.append("Custom")
	decision = moose.askOption("Choose a scenario:", scenarioDisp)
	if scenarioDisp[decision - 1] != "Custom":
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
			class gameData:
				scenCar = loadedScenario["gamedata"]["vehicle"]
				director = loadedScenario["gamedata"]["director"]
				food = loadedScenario["gamedata"]["food"]
				water = loadedScenario["gamedata"]["water"]
				twinkies = loadedScenario["gamedata"]["twinkies"]
				radiation = loadedScenario["gamedata"]["radiation"]
				bandits = loadedScenario["gamedata"]["bandits"]
				end = loadedScenario["journeylength"]
			class gameTime:
				seconds = 0
				minutes = random.randint(0, 59)
				hours = random.randint(1, 12)
				days = loadedScenario["day"]
				months = loadedScenario["month"]
				years = loadedScenario["year"]
			class character:
				hunger = 100
				thirst = 100
				health = 100
			currentCar = vehicle.loadCar(gameData.scenCar, vehicles, items)
			gameLoop()
		if decision == 2:
			print(moose.format.clear)
			startGame()
	else:
		class gameData:
			scenCar = "cav_alm1"
			director = "choice"
			food = 1
			water = 1
			twinkies = 1
			radiation = 1
			bandits = 1
			end = 500
		class gameTime:
			seconds = 0
			minutes = random.randint(0, 59)
			hours = random.randint(1, 12)
			days = 6
			months = 7
			years = 2013
		class character:
			hunger = 100
			thirst = 100
			health = 100
			inventory = []
		menus = ["Distance", "Starting vehicle", "Start game"]
		x = 0
		while menus[x] != "Start game":
			print(moose.format.clear)
			y = 0
			print("  ", end = "| ")
			while y < len(menus):
				if y == x:
					print(moose.format.bold, end = "")
				print(menus[y], end = "")
				print(moose.format.end, end = " | ")
				y = y + 1
			print()
			if menus[x] == "Distance":
				print("  Current distance: " + str(gameData.end))
			if menus[x] == "Starting vehicle":
				print("  Current vehicle: " + vehicles[gameData.scenCar]["name"])
			decision = moose.askString("Press enter to edit a variable, and use \"[\" and \"]\" keys to switch menus.")
			if decision == "[" and x - 1 >= 0:
				x = x - 1
			if decision == "]" and x + 1 <= len(menus) - 1:
				x = x + 1
			if decision != "[" and decision != "]":
				if menus[x] == "Distance":
					gameData.end = moose.askOpen("Set distance for the journey: ", min = 0)
				if menus[x] == "Starting vehicle":
					displayVehicles = []
					y = 0
					while y < len(vehicles["list"]):
						displayVehicles.append(vehicles[vehicles["list"][y]]["name"])
						y = y + 1
					decision = moose.askOption("Select vehicle", displayVehicles)
					gameData.scenCar = vehicles["list"][decision - 1]
		currentCar = vehicle.loadCar(gameData.scenCar, vehicles, items)
		print(moose.format.clear)
		gameLoop()

def gameLoop():
	action = moose.askOption("")

init()