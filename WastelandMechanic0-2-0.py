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
"""

#Made by Flint
#Project start: August 26, 2021
#Project end: Not any time soon
#Version number: v0.2 (RELEASE)

"""
Commenting conventions in this program:
- Comments before function w/ dependancies & dependants
- Comments within program describing flow
"""

"""
v0.2 includes the following that v0.1 didn't:
- SAVING! Just be sure to remember your save file name.
- Special events
- 3 cars under the Highlander brand
    - Based on Jeep vehicles
- 3 cars under the Fortuna brand
    - Based on Volkswagen vehicles
- 2 new cars under the Roach nameplate
    - Loosely based on the likes of the peel-50 and other extreme compacts
- Little bit more story in the introductory sequence
- Code comments
"""

import random
import time
import pickle
rand = 0
loop = 0
remove = 0
plrinput = 0
#If something doesn't work set debug to 1 and it might print debug statements as the program runs
#Please send screenshots of what runs right before the error to me via discord or github
debug = 0
#If you don't wanna waste 10 seconds of your life each time you run this thing make this have a value of 1
bypassIntro = 1
money = 500
minutes = 0
minutesStr = ""
hours = 12
day = 156



#Saves current variables into a pickle file
#Dependancies: pickle
#Dependants: checkWorkOrder()
def saveProgress():
    #Prompts user
    print("What would you like this save file to be named?")
    plrinput = input("\n>>> ")
    plrinput = str(plrinput)
    #Creates save name with prefix
    save = plrinput + ".p"
    #Puts all current data into one object
    data = [money, carID, carEngine, carRadiator, carTransmission, carTire1, carTire2, carTire3, carTire4, carBattery, carFuelTank, carHeadlight1, carHeadlight2, carTailLight1, carTailLight2, carLine1, carLine2, carLine3, carLine4, carLine5, carLine6, carLine7, carLine8, carLine9, carLine10, carLine11, carLine12, carLine13, carLine14, carLine15, carLine16, carLine17, carLine18, reqCode, carName, carSuspension1, carSuspension2, carSuspension3, carSuspension4, carRadio, moneySpent, hours, minutes, day]
    #Dumps object
    pickle.dump(data, open(save, "wb"))
    print("Progress saved.")
    #Returns flow
    drawInspectionMenu()



#Loads previous variables from a pickle file
#Dependancies: pickle, chanceCarGraphics(), drawInspectionMenu()
#Dependants: main
def loadProgress():
    #Globalizes all variables loaded
    global money
    global reqCode
    global carID
    global carName
    global carLine1
    global carLine2
    global carLine3
    global carLine4
    global carLine5
    global carLine6
    global carLine7
    global carLine8
    global carLine9
    global carLine10
    global carLine11
    global carLine12
    global carLine13
    global carLine14
    global carLine15
    global carLine16
    global carLine17
    global carLine18
    global carEngine
    global carRadiator
    global carTransmission
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carSuspension1
    global carSuspension2
    global carSuspension3
    global carSuspension4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2
    global carRadio
    global moneySpent
    global hours
    global minutes
    global day
    
    #User warning
    print("What save file would you like to load?\n")
    print("WARNING: Do NOT load a file given to you by someone! Pickle")
    print("is a very unsecure module, and may be used by someone to")
    print("run unwanted code on your computer. I'll try to make")
    print("it so data will be encoded to JSON in later versons.\n")
    plrinput = input("\n>>> ")
    plrinput = str(plrinput)
    #Creates file search name
    save = plrinput + ".p"
    #Finds save file
    data = pickle.load(open(save, "rb"))
    if debug == 1:
        print(len(data))

    #Sets global to saved data
    money = data[0]
    carID = data[1]
    carEngine = data[2]
    carRadiator = data[3]
    carTransmission = data[4]
    carTire1 = data[5]
    carTire2 = data[6]
    carTire3 = data[7]
    carTire4 = data[8]
    carBattery = data[9]
    carFuelTank = data[10]
    carHeadlight1 = data[11]
    carHeadlight2 = data[12]
    carTailLight1 = data[13]
    carTailLight2 = data[14]
    carLine1 = data[15]
    carLine2 = data[16]
    carLine3 = data[17]
    carLine4 = data[18]
    carLine5 = data[19]
    carLine6 = data[20]
    carLine7 = data[21]
    carLine8 = data[22]
    carLine9 = data[23]
    carLine10 = data[24]
    carLine11 = data[25]
    carLine12 = data[26]
    carLine13 = data[27]
    carLine14 = data[28]
    carLine15 = data[29]
    carLine16 = data[30]
    carLine17 = data[31]
    carLine18 = data[32]
    reqCode = data[33]
    carName = data[34]
    carSuspension1 = data[35]
    carSuspension2 = data[36]
    carSuspension3 = data[37]
    carSuspension4 = data[38]
    carRadio = data[39]
    moneySpent = data[40]
    hours = data[41]
    minutes = data[42]
    day = data[43]

    print("Progress loaded.")
    #Returns flow
    changeCarGraphics()
    drawInspectionMenu()



#Updates display time
#Dependancies: none
#Dependants: makeWorkOrder(), drawInspectionMenu()
def updateTime():
    global hours
    global minutes
    global minutesStr
    global day

    while minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1

    while hours >= 24:
        hours = hours - 24
        day = day + 1

    if minutes < 10:
        minutesStr = "0" + str(minutes)
    else:
        minutesStr = str(minutes)
        


#Changes the appearance of the vehicle sprite
#Dependancies: none
#Dependants: makeWorkOrder(), drawInspectionMenu(), loadProgress()
def changeCarGraphics():
    #Globalizes display variables
    global plrinput
    global carID
    global carLine1
    global carLine2
    global carLine3
    global carLine4
    global carLine5
    global carLine6
    global carLine7
    global carLine8
    global carLine9
    global carLine10
    global carLine11
    global carLine12
    global carLine13
    global carLine14
    global carLine15
    global carLine16
    global carLine17
    global carLine18
    global carEngine
    global carRadiator1
    global carTransmission
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2

    if debug == 1:
        print("changeCarGraphics() run!")

    #This gets VERY repetative. I'm just gonna write for the first one.

    #Finds car
    if carID == "CAV_ALM1":
        if debug == 1:
            print("carID read!")

        #Checks for tire 1+2 damage and changes display variables accordingly
        if carTire1 != "None" and carTire2 != "None":
            carLine6 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine6 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine6 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine6 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")

        #Checks for tire 3+4 damage and changes display variables accordingly
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        #Checks for headlight damage and changes display variables accordingly
        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine7 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine7 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine7 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine7 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        #Checks for tail light damage and changes display variables accordingly
        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_ALM2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine6 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine6 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine6 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine6 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine7 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine7 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine7 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine7 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_TRACER":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")
                
        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_OMEGA":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_CAP":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_SAT1":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_SAT2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")    
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_GEM":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")

        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_M7":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║│┆┆┆┆│║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║│┆┆┆┆│x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x│┆┆┆┆│║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x│┆┆┆┆│x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌┬────┬┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌┬────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x────┬┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_M9":
        if debug == 1:
            print("carID read!")
            
        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║│┆┆┆┆│║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║│┆┆┆┆│x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x│┆┆┆┆│║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x│┆┆┆┆│x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌┬────┬┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌┬────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x────┬┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_M11":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║│┆┆┆┆│║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║│┆┆┆┆│x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x│┆┆┆┆│║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x│┆┆┆┆│x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭┬────┬╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭┬────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x────┬╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_MSS":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║  --  ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║  --  x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x  --  ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x  --  x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║│┆┆┆┆│║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║│┆┆┆┆│x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x│┆┆┆┆│║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x│┆┆┆┆│x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭┬────┬╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭┬────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x────┬╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_C4":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_RO1":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_RO2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine8 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine8 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine8 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine8 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine9 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine9 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine9 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine9 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_CAM2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "╟──────╢"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "╟──────x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x──────╢"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x──────x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_CAM3":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "╟──────╢"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "╟──────x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x──────╢"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x──────x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "CAV_CAM4":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine3 = "╟──────╢"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine3 = "╟──────x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine3 = "x──────╢"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine3 = "x──────x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "HIL_WRE":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║┌────┐║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║┌────┐x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x┌────┐║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x┌────┐x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "HIL_COM1":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "HIL_COM2":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║      ║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║      x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x      ║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x      x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "FOR_SCR":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "╟──────╢"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "╟──────x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x──────╢"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x──────x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "FOR_JET":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║      ║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║      x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x      ║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x      x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "╟──────╢"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "╟──────x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x──────╢"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x──────x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "└──────┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "└─────x┘"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "└x─────┘"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "└x────x┘"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌──────┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌─────x┐"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x─────┐"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x────x┐"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "FOR_BUG":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine7 = "║╎    ╎║"
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine7 = "║╎    ╎x"
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine7 = "x╎    ╎║"
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine7 = "x╎    ╎x"
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "║╎    ╎║"
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "║╎    ╎x"
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x╎    ╎║"
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x╎    ╎x"
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰──────╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰─────x╯"
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x─────╯"
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x────x╯"
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "╭──────╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "╭─────x╮"
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "╭x─────╮"
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "╭x────x╮"
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "RCH_500":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine4 = "╟───╢   "
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine4 = "╟───x   "
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine4 = "x───╢   "
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine4 = "x───x   "
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "╟───╢   "
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "╟───x   "
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x───╢   "
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x───x   "
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰───╯   "
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰──x╯   "
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x──╯   "
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x─x╯   "
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌───┐   "
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌──x┐   "
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x──┐   "
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x─x┐   "
            if debug == 1:
                print("carTailLight1+2 graphics updated!")

    if carID == "RCH_700":
        if debug == 1:
            print("carID read!")

        if carTire1 != "None" and carTire2 != "None":
            carLine4 = "║┌─┐║   "
            if debug == 1:
                print("carTire1+2 graphics updated!")
        if carTire1 == "None":
            carLine4 = "║┌─┐x   "
            if debug == 1:
                print("carTire1 graphics updated!")
        if carTire2 == "None":
            carLine4 = "x┌─┐║   "
            if debug == 1:
                print("carTire2 graphics updated!")
        if carTire1 == "None" and carTire2 == "None":
            carLine4 = "x┌─┐x   "
            if debug == 1:
                print("carTire1+2 graphics updated!")
                
        if carTire3 != "None" and carTire4 != "None":
            carLine2 = "╟───╢   "
            if debug == 1:
                print("carTire3+4 graphics updated!")
        if carTire3 == "None":
            carLine2 = "╟───x   "
            if debug == 1:
                print("carTire3 graphics updated!")
        if carTire4 == "None":
            carLine2 = "x───╢   "
            if debug == 1:
                print("carTire4 graphics updated!")
        if carTire3 == "None" and carTire4 == "None":
            carLine2 = "x───x   "
            if debug == 1:
                print("carTire3+4 graphics updated!")

        if carHeadlight1 != "None" and carHeadlight2 != "None":
            carLine8 = "╰───╯   "
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")
        if carHeadlight1 == "None":
            carLine8 = "╰──x╯   "
            if debug == 1:
                print("carHeadlight1 graphics updated!")
        if carHeadlight2 == "None":
            carLine8 = "╰x──╯   "
            if debug == 1:
                print("carHeadlight2 graphics updated!")
        if carHeadlight1 == "None" and carHeadlight2 == "None":
            carLine8 = "╰x─x╯   "
            if debug == 1:
                print("carHeadlight1+2 graphics updated!")

        if carTailLight1 != "None" and carTailLight2 != "None":
            carLine1 = "┌───┐   "
            if debug == 1:
                print("carTailLight1+2 graphics updated!")
        if carTailLight1 == "None":
            carLine1 = "┌──x┐   "
            if debug == 1:
                print("carTailLight1 graphics updated!")
        if carTailLight2 == "None":
            carLine1 = "┌x──┐   "
            if debug == 1:
                print("carTailLight2 graphics updated!")
        if carTailLight1 == "None" and carTailLight2 == "None":
            carLine1 = "┌x─x┐   "
            if debug == 1:
                print("carTailLight1+2 graphics updated!")



#Opens the modification menu
#Dependancies: random, drawInspectionMenu(), checkManual()
#Dependants: makeWorkOrder(), drawInspectionMenu()
def modifyCar():
    #Globalizes all variables
    global money
    global moneySpent
    global plrinput
    global tiresChanged
    global carID
    global carName
    global carLine1
    global carLine2
    global carLine3
    global carLine4
    global carLine5
    global carLine6
    global carLine7
    global carLine8
    global carLine9
    global carLine10
    global carLine11
    global carLine12
    global carLine13
    global carLine14
    global carLine15
    global carLine16
    global carLine17
    global carLine18
    global carStorage1
    global carStorage2
    global carStorage3
    global carStorage4
    global carStorage5
    global carStorage6
    global carStorage7
    global carStorage8
    global carStorage9
    global carStorage10
    global carStorage11
    global carStorage12
    global carStorage13
    global carStorage14
    global carStorage15
    global carStorage16
    global carEngine
    global carRadiator
    global carTransmission
    global carSuspension1
    global carSuspension2
    global carSuspension3
    global carSuspension4
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2
    global carRadio
    global minutes
    plrinput = int(plrinput)
    
    #Prints all branches and their current parts
    print("  " + "Select a vehicle slot.")
    print("  " + " 1. Engine - " + carEngine)
    print("  " + " 2. Radiator - " + carRadiator)
    print("  " + " 3. Transmission - " + carTransmission)
    print("  " + " 4. FL suspension - " + carSuspension1)
    print("  " + " 5. FR suspension - " + carSuspension2)
    print("  " + " 6. RL suspension - " + carSuspension3)
    print("  " + " 7. RR suspension - " + carSuspension4)
    print("  " + " 8. FL tire - " + carTire1)
    print("  " + " 9. FR tire - " + carTire2)
    print("  " + "10. RL tire - " + carTire3)
    print("  " + "11. RR tire - " + carTire4)
    print("  " + "12. Battery - " + carBattery)
    print("  " + "13. Fuel tank - " + carFuelTank)
    print("  " + "14. L headlight - " + carHeadlight1)
    print("  " + "15. R headlight - " + carHeadlight2)
    print("  " + "16. L tail light - " + carTailLight1)
    print("  " + "17. R tail light - " + carTailLight2)
    print("  " + "18. Radio - " + carRadio)
    print("\n  " + "19. Check manual")
    print("  " + "20. Exit")

    #Also very repetative. Only doing one.

    #Finds initial branch
    plrinput = input("\n>>> ")
    plrinput = int(plrinput)
    if plrinput == 1:
        #Prints part options
        print("  " + "Select an engine.")
        print("  " + " 1. Low liter engine  - 150$")
        print("  " + " 2. Economy engine    - 300$")
        print("  " + " 3. Regular engine    - 500$")
        print("  " + " 4. Sport engine      - 750$")
        print("  " + " 5. Heavy duty engine - 850$")
        print("  " + " 6. Remove engine")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        
        #Finds part branch
        if plrinput == 1:
            #Sets part
            carEngine = "Low liter engine"
            #Subtracts money
            money = money - 150
            #Adds to moneySpent
            moneySpent = moneySpent + 150
            #Changes time
            minutes = minutes + random.randint(40, 70)
        if plrinput == 2:
            carEngine = "Economy engine"
            money = money - 300
            moneySpent = moneySpent + 300
            minutes = minutes + random.randint(50, 85)
        if plrinput == 3:
            carEngine = "Regular engine"
            money = money - 500
            moneySpent = moneySpent + 500
            minutes = minutes + random.randint(60, 90)
        if plrinput == 4:
            carEngine = "Sport engine"
            money = money - 750
            moneySpent = moneySpent + 750
            minutes = minutes + random.randint(60, 120)
        if plrinput == 5:
            carEngine = "Heavy duty engine"
            money = money - 850
            moneySpent = moneySpent + 850
            minutes = minutes + random.randint(70, 120)
        if plrinput == 6:
            carEngine = "None"
            minutes = minutes + random.randint(50, 80)
        plrinput = 0
    if plrinput == 2:
        print("  " + "Select a radiator.")
        print("  " + " 1. Economy radiator     - 100$")
        print("  " + " 2. Regular radiator     - 200$")
        print("  " + " 3. Performance radiator - 350$")
        print("  " + " 4. Heavy duty radiator  - 400$")
        print("  " + " 5. Remove radiator")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carRadiator = "Economy radiator"
            money = money - 100
            moneySpent = moneySpent + 100
            minutes = minutes + random.randint(20, 40)
        if plrinput == 2:
            carRadiator = "Regular radiator"
            money = money - 200
            moneySpent = moneySpent + 200
            minutes = minutes + random.randint(20, 50)
        if plrinput == 3:
            carRadiator = "Performance radiator"
            money = money - 350
            moneySpent = moneySpent + 350
            minutes = minutes + random.randint(30, 50)
        if plrinput == 4:
            carRadiator = "Heavy duty radiator"
            money = money - 400
            moneySpent = moneySpent + 400
            minutes = minutes + random.randint(30, 60)
        if plrinput == 5:
            carRadiator = "None"
            minutes = minutes + random.randint(25, 45)
        plrinput = 0
    if plrinput == 3:
        print("  " + "Select a transmission.")
        print("  " + " 1. Regular automatic    - 300$")
        print("  " + " 2. Sport automatic      - 500$")
        print("  " + " 3. Heavy duty automatic - 600$")
        print("  " + " 4. Regular manual       - 250$")
        print("  " + " 5. Sport manual         - 400$")
        print("  " + " 6. Heavy duty manual    - 500$")
        print("  " + " 7. Remove transmission")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTransmission = "Regular automatic"
            money = money - 300
            moneySpent = moneySpent + 300
            minutes = minutes + random.randint(40, 60)
        if plrinput == 2:
            carTransmission = "Sport automatic"
            money = money - 500
            moneySpent = moneySpent + 500
            minutes = minutes + random.randint(45, 70)
        if plrinput == 3:
            carTransmission = "Heavy duty automatic"
            money = money - 600
            moneySpent = moneySpent + 600
            minutes = minutes + random.randint(55, 80)
        if plrinput == 4:
            carTransmission = "Regular manual"
            money = money - 250
            moneySpent = moneySpent + 250
            minutes = minutes + random.randint(30, 50)
        if plrinput == 5:
            carTransmission = "Sport manual"
            money = money - 400
            moneySpent = moneySpent + 400
            minutes = minutes + random.randint(35, 60)
        if plrinput == 6:
            carTransmission = "Heavy duty manual"
            money = money - 500
            moneySpent = moneySpent + 500
            minutes = minutes + random.randint(45, 70)
        if plrinput == 6:
            carTransmission = "None"
            minutes = minutes + random.randint(30, 50)
        plrinput = 0
    if plrinput == 4:
        print("  " + "Select a suspension kit.")
        print("  " + " 1. City suspension       - 100$")
        print("  " + " 2. Lowrider suspension   - 175$")
        print("  " + " 3. Offroad suspension    - 200$")
        print("  " + " 4. Heavy duty suspension - 400$")
        print("  " + " 5. Remove suspension")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carSuspension1 = "City suspension"
            money = money - 100
            moneySpent = moneySpent + 100
            minutes = minutes + random.randint(30, 40)
        if plrinput == 2:
            carSuspension1 = "Lowrider suspension"
            money = money - 175
            moneySpent = moneySpent + 175
            minutes = minutes + random.randint(35, 55)
        if plrinput == 3:
            carSuspension1 = "Offroad suspension"
            money = money - 200
            moneySpent = moneySpent + 200
            minutes = minutes + random.randint(50, 75)
        if plrinput == 4:
            carSuspension1 = "Heavy duty suspension"
            money = money - 400
            moneySpent = moneySpent + 400
            minutes = minutes + random.randint(50, 70)
        if plrinput == 5:
            carSuspension1 = "None"
            minutes = minutes + random.randint(35, 50)
        plrinput = 0
    if plrinput == 5:
        print("  " + "Select a suspension kit.")
        print("  " + " 1. City suspension       - 100$")
        print("  " + " 2. Lowrider suspension   - 175$")
        print("  " + " 3. Offroad suspension    - 200$")
        print("  " + " 4. Heavy duty suspension - 400$")
        print("  " + " 5. Remove suspension")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carSuspension2 = "City suspension"
            money = money - 100
            moneySpent = moneySpent + 100
            minutes = minutes + random.randint(30, 40)
        if plrinput == 2:
            carSuspension2 = "Lowrider suspension"
            money = money - 175
            moneySpent = moneySpent + 175
            minutes = minutes + random.randint(35, 55)
        if plrinput == 3:
            carSuspension2 = "Offroad suspension"
            money = money - 200
            moneySpent = moneySpent + 200
            minutes = minutes + random.randint(50, 75)
        if plrinput == 4:
            carSuspension2 = "Heavy duty suspension"
            money = money - 400
            moneySpent = moneySpent + 400
            minutes = minutes + random.randint(50, 70)
        if plrinput == 5:
            carSuspension2 = "None"
            minutes = minutes + random.randint(35, 50)
        plrinput = 0
    if plrinput == 6:
        print("  " + "Select a suspension kit.")
        print("  " + " 1. City suspension       - 100$")
        print("  " + " 2. Lowrider suspension   - 175$")
        print("  " + " 3. Offroad suspension    - 200$")
        print("  " + " 4. Heavy duty suspension - 400$")
        print("  " + " 5. Remove suspension")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carSuspension3 = "City suspension"
            money = money - 100
            moneySpent = moneySpent + 100
            minutes = minutes + random.randint(30, 40)
        if plrinput == 2:
            carSuspension3 = "Lowrider suspension"
            money = money - 175
            moneySpent = moneySpent + 175
            minutes = minutes + random.randint(35, 55)
        if plrinput == 3:
            carSuspension3 = "Offroad suspension"
            money = money - 200
            moneySpent = moneySpent + 200
            minutes = minutes + random.randint(50, 75)
        if plrinput == 4:
            carSuspension3 = "Heavy duty suspension"
            money = money - 400
            moneySpent = moneySpent + 400
            minutes = minutes + random.randint(50, 70)
        if plrinput == 5:
            carSuspension3 = "None"
            minutes = minutes + random.randint(35, 50)
        plrinput = 0
    if plrinput == 7:
        print("  " + "Select a suspension kit.")
        print("  " + " 1. City suspension       - 100$")
        print("  " + " 2. Lowrider suspension   - 175$")
        print("  " + " 3. Offroad suspension    - 200$")
        print("  " + " 4. Heavy duty suspension - 400$")
        print("  " + " 5. Remove suspension")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carSuspension4 = "City suspension"
            money = money - 100
            moneySpent = moneySpent + 100
            minutes = minutes + random.randint(30, 40)
        if plrinput == 2:
            carSuspension4 = "Lowrider suspension"
            money = money - 175
            moneySpent = moneySpent + 175
            minutes = minutes + random.randint(35, 55)
        if plrinput == 3:
            carSuspension4 = "Offroad suspension"
            money = money - 200
            moneySpent = moneySpent + 200
            minutes = minutes + random.randint(50, 75)
        if plrinput == 4:
            carSuspension4 = "Heavy duty suspension"
            money = money - 400
            moneySpent = moneySpent + 400
            minutes = minutes + random.randint(50, 70)
        if plrinput == 5:
            carSuspension4 = "None"
            minutes = minutes + random.randint(35, 50)
        plrinput = 0
    if plrinput == 8:
        print("  " + "Select a tire.")
        print("  " + " 1. Economy tire     - 75$")
        print("  " + " 2. Regular tire     - 125$")
        print("  " + " 3. Sport tire       - 200$")
        print("  " + " 4. Heavy duty tire  - 250$")
        print("  " + " 5. Offroad tire     - 300$")
        print("  " + " 6. Bulletproof tire - 400$")
        print("  " + " 7. Remove tire")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTire1 = "Economy tire"
            money = money - 75
            moneySpent = moneySpent + 75
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(25, 40)
        if plrinput == 2:
            carTire1 = "Regular tire"
            money = money - 125
            moneySpent = moneySpent + 125
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(30, 40)
        if plrinput == 3:
            carTire1 = "Sport tire"
            money = money - 200
            moneySpent = moneySpent + 200
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(35, 45)
        if plrinput == 4:
            carTire1 = "Heavy duty tire"
            money = money - 250
            moneySpent = moneySpent + 250
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(35, 50)
        if plrinput == 5:
            carTire1 = "Offroad tire"
            money = money - 300
            moneySpent = moneySpent + 300
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(40, 55)
        if plrinput == 6:
            carTire1 = "Bulletproof tire"
            money = money - 400
            moneySpent = moneySpent + 400
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(50, 70)
        if plrinput == 7:
            carTire1 = "None"
            minutes = minutes + random.randint(15, 20)
        plrinput = 0
    if plrinput == 9:
        print("  " + "Select a tire.")
        print("  " + " 1. Economy tire     - 75$")
        print("  " + " 2. Regular tire     - 125$")
        print("  " + " 3. Sport tire       - 200$")
        print("  " + " 4. Heavy duty tire  - 250$")
        print("  " + " 5. Offroad tire     - 300$")
        print("  " + " 6. Bulletproof tire - 400$")
        print("  " + " 7. Remove tire")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTire2 = "Economy tire"
            money = money - 75
            moneySpent = moneySpent + 75
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(25, 40)
        if plrinput == 2:
            carTire2 = "Regular tire"
            money = money - 125
            moneySpent = moneySpent + 125
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(30, 40)
        if plrinput == 3:
            carTire2 = "Sport tire"
            money = money - 200
            moneySpent = moneySpent + 200
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(35, 45)
        if plrinput == 4:
            carTire2 = "Heavy duty tire"
            money = money - 250
            moneySpent = moneySpent + 250
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(35, 50)
        if plrinput == 5:
            carTire2 = "Offroad tire"
            money = money - 300
            moneySpent = moneySpent + 300
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(40, 55)
        if plrinput == 6:
            carTire2 = "Bulletproof tire"
            money = money - 400
            moneySpent = moneySpent + 400
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(50, 70)
        if plrinput == 7:
            carTire2 = "None"
            minutes = minutes + random.randint(15, 20)
        plrinput = 0
    if plrinput == 10:
        print("  " + "Select a tire.")
        print("  " + " 1. Economy tire     - 75$")
        print("  " + " 2. Regular tire     - 125$")
        print("  " + " 3. Sport tire       - 200$")
        print("  " + " 4. Heavy duty tire  - 250$")
        print("  " + " 5. Offroad tire     - 300$")
        print("  " + " 6. Bulletproof tire - 400$")
        print("  " + " 7. Remove tire")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTire3 = "Economy tire"
            money = money - 75
            moneySpent = moneySpent + 75
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(25, 40)
        if plrinput == 2:
            carTire3 = "Regular tire"
            money = money - 125
            moneySpent = moneySpent + 125
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(30, 40)
        if plrinput == 3:
            carTire3 = "Sport tire"
            money = money - 200
            moneySpent = moneySpent + 200
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(35, 45)
        if plrinput == 4:
            carTire3 = "Heavy duty tire"
            money = money - 250
            moneySpent = moneySpent + 250
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(35, 50)
        if plrinput == 5:
            carTire3 = "Offroad tire"
            money = money - 300
            moneySpent = moneySpent + 300
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(40, 55)
        if plrinput == 6:
            carTire3 = "Bulletproof tire"
            money = money - 400
            moneySpent = moneySpent + 400
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(50, 70)
        if plrinput == 7:
            carTire3 = "None"
            minutes = minutes + random.randint(15, 20)
        plrinput = 0
    if plrinput == 11:
        print("  " + "Select a tire.")
        print("  " + " 1. Economy tire     - 75$")
        print("  " + " 2. Regular tire     - 125$")
        print("  " + " 3. Sport tire       - 200$")
        print("  " + " 4. Heavy duty tire  - 250$")
        print("  " + " 5. Offroad tire     - 300$")
        print("  " + " 6. Bulletproof tire - 400$")
        print("  " + " 7. Remove tire")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTire4 = "Economy tire"
            money = money - 75
            moneySpent = moneySpent + 75
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(25, 40)
        if plrinput == 2:
            carTire4 = "Regular tire"
            money = money - 125
            moneySpent = moneySpent + 125
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(30, 40)
        if plrinput == 3:
            carTire4 = "Sport tire"
            money = money - 200
            moneySpent = moneySpent + 200
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(35, 45)
        if plrinput == 4:
            carTire4 = "Heavy duty tire"
            money = money - 250
            moneySpent = moneySpent + 250
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(35, 50)
        if plrinput == 5:
            carTire4 = "Offroad tire"
            money = money - 300
            moneySpent = moneySpent + 300
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(40, 55)
        if plrinput == 6:
            carTire4 = "Bulletproof tire"
            money = money - 400
            moneySpent = moneySpent + 400
            tiresChanged = tiresChanged + 1
            minutes = minutes + random.randint(50, 70)
        if plrinput == 7:
            carTire4 = "None"
            minutes = minutes + random.randint(15, 20)
        plrinput = 0
    if plrinput == 12:
        print("  " + "Select a battery.")
        print("  " + " 1. Economy battery     - 100$")
        print("  " + " 2. Low charge battery  - 150$")
        print("  " + " 3. Regular battery     - 200$")
        print("  " + " 4. High charge battery - 300$")
        print("  " + " 5. Heavy duty battery  - 350$")
        print("  " + " 6. Remove battery")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carBattery = "Economy battery"
            money = money - 100
            moneySpent = moneySpent + 100
        if plrinput == 2:
            carBattery = "Low charge battery"
            money = money - 150
            moneySpent = moneySpent + 150
        if plrinput == 3:
            carBattery = "Regular battery"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 4:
            carBattery = "High charge battery"
            money = money - 300
            moneySpent = moneySpent + 300
        if plrinput == 5:
            carBattery = "Heavy duty battery"
            money = money - 350
            moneySpent = moneySpent + 350
        if plrinput == 6:
            carBattery = "None"
        plrinput = 0
    if plrinput == 13:
        print("  " + "Select a fuel tank.")
        print("  " + " 1. Low capacity tank  - 75$")
        print("  " + " 2. Regular tank       - 150$")
        print("  " + " 3. High capacity tank - 300$")
        print("  " + " 4. Heavy duty tank    - 325$")
        print("  " + " 5. Remove tank")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carFuelTank = "Low capacity tank"
            money = money - 75
            moneySpent = moneySpent + 75
        if plrinput == 2:
            carFuelTank = "Regular tank"
            money = money - 150
            moneySpent = moneySpent + 150
        if plrinput == 3:
            carFuelTank = "High capacity tank"
            money = money - 300
            moneySpent = moneySpent + 300
        if plrinput == 4:
            carFuelTank = "Heavy duty tank"
            money = money - 325
            moneySpent = moneySpent + 325
        if plrinput == 5:
            carFuelTank = "None"
        plrinput = 0
    if plrinput == 14:
        print("  " + "Select a headlight.")
        print("  " + " 1. Regular headlight    - 50$")
        print("  " + " 2. Xenon headlight      - 200$")
        print("  " + " 3. Reinforced headlight - 250$")
        print("  " + " 4. Remove headlight")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carHeadlight1 = "Regular headlight"
            money = money - 50
            moneySpent = moneySpent + 50
        if plrinput == 2:
            carHeadlight1 = "Xenon headlight"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carHeadlight1 = "Reinforced headlight"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 4:
            carHeadlight1 = "None"
        plrinput = 0
    if plrinput == 15:
        print("  " + "Select a headlight.")
        print("  " + " 1. Regular headlight    - 50$")
        print("  " + " 2. Xenon headlight      - 200$")
        print("  " + " 3. Reinforced headlight - 250$")
        print("  " + " 4. Remove headlight")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carHeadlight2 = "Regular headlight"
            money = money - 50
            moneySpent = moneySpent + 50
        if plrinput == 2:
            carHeadlight2 = "Xenon headlight"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carHeadlight2 = "Reinforced headlight"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 4:
            carHeadlight2 = "None"
        plrinput = 0
    if plrinput == 16:
        print("  " + "Select a tail light.")
        print("  " + " 1. Regular tail light    - 50$")
        print("  " + " 2. LED tail light        - 200$")
        print("  " + " 3. Reinforced tail light - 250$")
        print("  " + " 4. Remove tail light")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTailLight1 = "Regular tail light"
            money = money - 50
            moneySpent = moneySpent + 50
        if plrinput == 2:
            carTailLight1 = "LED tail light"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carTailLight1 = "Reinforced tail light"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 4:
            carTailLight1 = "None"
        plrinput = 0
    if plrinput == 17:
        print("  " + "Select a tail light.")
        print("  " + " 1. Regular tail light    - 50$")
        print("  " + " 2. LED tail light        - 200$")
        print("  " + " 3. Reinforced tail light - 250$")
        print("  " + " 4. Remove tail light")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carTailLight2 = "Regular tail light"
            money = money - 50
            moneySpent = moneySpent + 50
        if plrinput == 2:
            carTailLight2 = "LED tail light"
            money = money - 200
            moneySpent = moneySpent + 200
        if plrinput == 3:
            carTailLight2 = "Reinforced tail light"
            money = money - 250
            moneySpent = moneySpent + 250
        if plrinput == 4:
            carTailLight2 = "None"
        plrinput = 0
    if plrinput == 18:
        print("  " + "Select a radio.")
        print("  " + " 1. Commuter radio - 150$")
        print("  " + " 2. CB radio       - 325$")
        print("  " + " 3. Military radio - 1000$")
        print("  " + " 4. Remove radio")
        plrinput = input("\n>>> ")
        plrinput = int(plrinput)
        if plrinput == 1:
            carRadio = "Commuter radio"
            money = money - 150
            moneySpent = moneySpent + 150
        if plrinput == 2:
            carRadio = "CB radio"
            money = money - 325
            moneySpent = moneySpent + 325
        if plrinput == 3:
            carRadio = "Military radio"
            money = money - 1000
            moneySpent = moneySpent + 1000
        if plrinput == 4:
            carRadio = "None"
        plrinput = 0
    if plrinput == 19:
        checkManual(carID, 1)
    if plrinput == 20:
        if money < 0:
            print("\n  You leave the scrap yard after giving the manager an I.O.U.")
            time.sleep(1)
        drawInspectionMenu()



#Updates display time
#Dependancies: none
#Dependants: checkVehicle(), eventHandler()
def generateWorkCar():
    global moneySpent
    global plrinput
    global carID
    global carName
    global carLine1
    global carLine2
    global carLine3
    global carLine4
    global carLine5
    global carLine6
    global carLine7
    global carLine8
    global carLine9
    global carLine10
    global carLine11
    global carLine12
    global carLine13
    global carLine14
    global carLine15
    global carLine16
    global carLine17
    global carLine18
    global carEngine
    global carRadiator
    global carTransmission
    global carSuspension1
    global carSuspension2
    global carSuspension3
    global carSuspension4
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2
    global carRadio
    if debug == 1:
        print("generateWorkCar variables globalized!")
    rand = random.randint(1, 24)
    if debug == 1:
        print("rand randomized!")

    #Copies vehicle template
    if rand == 1:
        carID = "CAV_ALM1"
        carName = "1st GEN CAVICE ALMADA"
         
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "│      │"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "║      ║"
        carLine7 = "└──────┘"
        carLine8 = "        "
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Economy engine"
        carRadiator = "Economy radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Economy tire"
        carTire2 = "Economy tire"
        carTire3 = "Economy tire"
        carTire4 = "Economy tire"
        carBattery = "Economy battery"
        carFuelTank = "Low capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")


    if rand == 2:
        carID = "CAV_ALM2"
        carName = "2nd GEN CAVICE ALMADA"
         
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "│┌─┐┌─┐│"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "║      ║"
        carLine7 = "└──────┘"
        carLine8 = "        "
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "
        
        carEngine = "Economy engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Economy tire"
        carTire2 = "Economy tire"
        carTire3 = "Economy tire"
        carTire4 = "Economy tire"
        carBattery = "Economy battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 3:
        carID = "CAV_TRACER"
        carName = "CAVICE TRACER"
         
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│┌────┐│"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 4:
        carID = "CAV_OMEGA"
        carName = "CAVICE OMEGA"
         
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 5:
        carID = "CAV_CAP"
        carName = "CAVICE CAPACITY"
         
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "│┌────┐│"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "High capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 6:
        carID = "CAV_SAT1"
        carName = "1st GEN CAVICE SATELLITE"
         
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│      │"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Sport tire"
        carTire2 = "Sport tire"
        carTire3 = "Sport tire"
        carTire4 = "Sport tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 7:
        carID = "CAV_SAT2"
        carName = "2nd GEN CAVICE SATELLITE"
         
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│      │"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Sport tire"
        carTire2 = "Sport tire"
        carTire3 = "Sport tire"
        carTire4 = "Sport tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Xenon headlight"
        carHeadlight2 = "Xenon headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 8:
        carID = "CAV_GEM"
        carName = "CAVICE GEMINI"
         
        carLine1 = "╭──────╮"
        carLine2 = "║      ║"
        carLine3 = "├──────┤"
        carLine4 = "│ ┌──┐ │"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Sport tire"
        carTire2 = "Sport tire"
        carTire3 = "Sport tire"
        carTire4 = "Sport tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Xenon headlight"
        carHeadlight2 = "Xenon headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 9:
        carID = "CAV_M7"
        carName = "7th GEN CAVICE M-SERIES"
         
        carLine1 = "┌┬────┬┐"
        carLine2 = "││┆┆┆┆││"
        carLine3 = "║│┆┆┆┆│║"
        carLine4 = "│└────┘│"
        carLine5 = "├──────┤"
        carLine6 = "│┌────┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "└──────┘"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Heavy duty radiator"
        carTransmission = "Regular manual"
        carSuspension1 = "Offroad suspension"
        carSuspension2 = "Offroad suspension"
        carSuspension3 = "Offroad suspension"
        carSuspension4 = "Offroad suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "None"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 10:
        carID = "CAV_M9"
        carName = "9th GEN CAVICE M-SERIES"
         
        carLine1 = "┌┬────┬┐"
        carLine2 = "││┆┆┆┆││"
        carLine3 = "║│┆┆┆┆│║"
        carLine4 = "││┆┆┆┆││"
        carLine5 = "├┴────┴┤"
        carLine6 = "│┌────┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "└──────┘"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Heavy duty radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "Offroad suspension"
        carSuspension2 = "Offroad suspension"
        carSuspension3 = "Offroad suspension"
        carSuspension4 = "Offroad suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 11:
        carID = "CAV_M11"
        carName = "11th GEN CAVICE M-SERIES"
         
        carLine1 = "╭┬────┬╮"
        carLine2 = "││┆┆┆┆││"
        carLine3 = "║│┆┆┆┆│║"
        carLine4 = "││┆┆┆┆││"
        carLine5 = "├┴────┴┤"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Heavy duty engine"
        carRadiator = "Heavy duty radiator"
        carTransmission = "Heavy duty automatic"
        carSuspension1 = "Heavy duty suspension"
        carSuspension2 = "Heavy duty suspension"
        carSuspension3 = "Heavy duty suspension"
        carSuspension4 = "Heavy duty suspension"
        carTire1 = "Heavy duty tire"
        carTire2 = "Heavy duty tire"
        carTire3 = "Heavy duty tire"
        carTire4 = "Heavy duty tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 12:
        carID = "CAV_MSS"
        carName = "CAVICE M-SERIES SUPER SWAMPER"
         
        carLine1 = "╭┬────┬╮"
        carLine2 = "││┆┆┆┆││"
        carLine3 = "║│┆┆┆┆│║"
        carLine4 = "││┆┆┆┆││"
        carLine5 = "├┴────┴┤"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║  --  ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "Heavy duty suspension"
        carSuspension2 = "Heavy duty suspension"
        carSuspension3 = "Heavy duty suspension"
        carSuspension4 = "Heavy duty suspension"
        carTire1 = "Offroad tire"
        carTire2 = "Offroad tire"
        carTire3 = "Offroad tire"
        carTire4 = "Offroad tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Xenon headlight"
        carHeadlight2 = "Xenon headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 13:
        carID = "CAV_C4"
        carName = "4th GEN CAVICE C-SERIES"
         
        carLine1 = "┌──────┐"
        carLine2 = "│      │"
        carLine3 = "║      ║"
        carLine4 = "│      │"
        carLine5 = "│      │"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Heavy duty engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "High capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "CB radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 14:
        carID = "CAV_RO1"
        carName = "1st GEN CAVICE ROAMER"
         
        carLine1 = "┌──────┐"
        carLine2 = "│┌────┐│"
        carLine3 = "║      ║"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│      │"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "High capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 15:
        carID = "CAV_RO2"
        carName = "2nd GEN CAVICE ROAMER"
         
        carLine1 = "╭──────╮"
        carLine2 = "│┌────┐│"
        carLine3 = "║      ║"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│      │"
        carLine6 = "│┌─┐┌─┐│"
        carLine7 = "├──────┤"
        carLine8 = "║      ║"
        carLine9 = "╰──────╯"
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "High capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 16:
        carID = "CAV_CAM2"
        carName = "2nd GEN CAVICE CAMBIO"
         
        carLine1 = "┌──────┐"
        carLine2 = "│      │"
        carLine3 = "╟──────╢"
        carLine4 = "│┌────┐│"
        carLine5 = "├──────┤"
        carLine6 = "│  --  │"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Sport manual"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "None"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 17:
        carID = "CAV_CAM3"
        carName = "3rd GEN CAVICE CAMBIO"
         
        carLine1 = "┌──────┐"
        carLine2 = "│ ==== │"
        carLine3 = "╟──────╢"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│      │"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 18:
        carID = "CAV_CAM4"
        carName = "4th GEN CAVICE CAMBIO"
         
        carLine1 = "╭──────╮"
        carLine2 = "│      │"
        carLine3 = "╟──────╢"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│  ==  │"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Performance radiator"
        carTransmission = "Sport automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 19:
        carID = "HIL_WRE"
        carName = "HIGHLANDER WRESTLER"
         
        carLine1 = "╭──────╮"
        carLine2 = "║┌────┐║"
        carLine3 = "│      │"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "├──────┤"
        carLine6 = "│      │"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Sport engine"
        carRadiator = "Heavy duty radiator"
        carTransmission = "Heavy duty automatic"
        carSuspension1 = "Offroad suspension"
        carSuspension2 = "Offroad suspension"
        carSuspension3 = "Offroad suspension"
        carSuspension4 = "Offroad suspension"
        carTire1 = "Offroad tire"
        carTire2 = "Offroad tire"
        carTire3 = "Offroad tire"
        carTire4 = "Offroad tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Xenon headlight"
        carHeadlight2 = "Xenon headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 20:
        carID = "HIL_COM1"
        carName = "1st GEN HIGHLANDER COMANCHE"
         
        carLine1 = "┌──────┐"
        carLine2 = "║      ║"
        carLine3 = "│┌────┐│"
        carLine4 = "│      │"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 21:
        carID = "HIL_COM2"
        carName = "2nd GEN HIGHLANDER COMANCHE"
         
        carLine1 = "╭──────╮"
        carLine2 = "║      ║"
        carLine3 = "│┌─┐┌─┐│"
        carLine4 = "│      │"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "High charge battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 22:
        carID = "FOR_SCR"
        carName = "FORTUNA SOCCER"
         
        carLine1 = "╭──────╮"
        carLine2 = "╟──────╢"
        carLine3 = "│┌─┐┌─┐│"
        carLine4 = "│      │"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Low capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "Regular tail light"
        carTailLight2 = "Regular tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 23:
        carID = "FOR_JET"
        carName = "FORTUNA JET"
         
        carLine1 = "┌──────┐"
        carLine2 = "╟──────╢"
        carLine3 = "│┌────┐│"
        carLine4 = "│      │"
        carLine5 = "│┌─┐┌─┐│"
        carLine6 = "├──────┤"
        carLine7 = "║      ║"
        carLine8 = "└──────┘"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Regular engine"
        carRadiator = "Regular radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Regular battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 24:
        carID = "FOR_BUG"
        carName = "FORTUNA BUG"
         
        carLine1 = "╭──────╮"
        carLine2 = "║╎    ╎║"
        carLine3 = "├──────┤"
        carLine4 = "│┌─┐┌─┐│"
        carLine5 = "│      │"
        carLine6 = "├──────┤"
        carLine7 = "║╎    ╎║"
        carLine8 = "╰──────╯"
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Economy engine"
        carRadiator = "Economy radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Regular tire"
        carTire2 = "Regular tire"
        carTire3 = "Regular tire"
        carTire4 = "Regular tire"
        carBattery = "Economy battery"
        carFuelTank = "Regular tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "Commuter radio"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 25:
        carID = "RCH_500"
        carName = "ROACH 500"
         
        carLine1 = "┌───┐   "
        carLine2 = "╟───╢   "
        carLine3 = "│┌─┐│   "
        carLine4 = "╟───╢   "
        carLine5 = "╰───╯   "
        carLine6 = "        "
        carLine7 = "        "
        carLine8 = "        "
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Low liter engine"
        carRadiator = "Economy radiator"
        carTransmission = "Regular manual"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Economy tire"
        carTire2 = "Economy tire"
        carTire3 = "Economy tire"
        carTire4 = "Economy tire"
        carBattery = "Economy battery"
        carFuelTank = "Low capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "None"
        if debug == 1:
            print("generateWorkCar variables set!")

    if rand == 26:
        carID = "RCH_700"
        carName = "ROACH 700"
         
        carLine1 = "┌───┐"
        carLine2 = "║┌─┐║"
        carLine3 = "│┌─┐│"
        carLine4 = "╟───╢"
        carLine5 = "╰───╯"
        carLine6 = "        "
        carLine7 = "        "
        carLine8 = "        "
        carLine9 = "        "
        carLine10 = "        "
        carLine11 = "        "
        carLine12 = "        "
        carLine13 = "        "
        carLine14 = "        "
        carLine15 = "        "
        carLine16 = "        "
        carLine17 = "        "
        carLine18 = "        "

        carEngine = "Low liter engine"
        carRadiator = "Economy radiator"
        carTransmission = "Regular automatic"
        carSuspension1 = "City suspension"
        carSuspension2 = "City suspension"
        carSuspension3 = "City suspension"
        carSuspension4 = "City suspension"
        carTire1 = "Economy tire"
        carTire2 = "Economy tire"
        carTire3 = "Economy tire"
        carTire4 = "Economy tire"
        carBattery = "Regular battery"
        carFuelTank = "Low capacity tank"
        carHeadlight1 = "Regular headlight"
        carHeadlight2 = "Regular headlight"
        carTailLight1 = "LED tail light"
        carTailLight2 = "LED tail light"
        carRadio = "None"
        if debug == 1:
            print("generateWorkCar variables set!")

    #Resets moneySpent
    moneySpent = 0
    #Returns flow
    makeWorkOrder()



#Updates display time
#Dependancies: none
#Dependants: generateWorkCar()
def makeWorkOrder():
    #Globalizes variables
    global requirement
    global formRequirement
    global reqCode
    global carEngine
    global carRadiator
    global carTransmission
    global carSuspension1
    global carSuspension2
    global carSuspension3
    global carSuspension4
    global carTire1
    global carTire2
    global carTire3
    global carTire4
    global carBattery
    global carFuelTank
    global carHeadlight1
    global carHeadlight2
    global carTailLight1
    global carTailLight2
    global carRadio
    ##I roll up to garaaaage yeeeeah
    global rollUp
    global tiresChanged

    #Randomly chooses roll up message
    rand = random.randint(1,100)
    if rand != 1:
        rollUp = "drives up to"
    if rand == 1:
        rollUp = "rolls up to"
    rand = random.randint(1, 10)

    if rand == 1:
        rand = random.randint(1,4)
        #Sets said requirement
        requirement = "replace one of the tires."
        #Adds form requirement
        formRequirement = "replace the flat tire."
        #Sets reqCode
        reqCode = "oneTire"
        #Resets tiresChanged
        tiresChanged = 0
        #Randomly selects and removes a tire.
        if rand == 1:
            carTire1 = "None"
        if rand == 2:
            carTire2 = "None"
        if rand == 3:
            carTire3 = "None"
        if rand == 4:
            carTire4 = "None"
        rand = 0

    if rand == 2:
        rand = random.randint(1,4)
        requirement = "replace some of the tires."
        formRequirement = "replace the two flat tires."
        reqCode = "oneTire"
        tiresChanged = 0
        if rand == 1:
            carTire1 = "None"
        if rand == 2:
            carTire2 = "None"
        if rand == 3:
            carTire3 = "None"
        if rand == 4:
            carTire4 = "None"
        rand = random.randint(1,4)
        if rand == 1:
            carTire1 = "None"
        if rand == 2:
            carTire2 = "None"
        if rand == 3:
            carTire3 = "None"
        if rand == 4:
            carTire4 = "None"
        rand = random.randint(1,10)
        if rand == 1:
            rollUp = "is towed into"
        if rand != 1:
            rollUp = "is pushed into"
        rand = 0
        
    if rand == 3:
        requirement = "replace the battery."
        formRequirement = "replace the dead battery."
        reqCode = "battery"
        carBattery = "Dead battery"
        rand = 0
        
    if rand == 4:
        requirement = "install a two way radio."
        formRequirement = "install a CB radio."
        reqCode = "cb"
        carRadio = "None"
        rand = 0
        
    if rand == 5:
        requirement = "replace the radiator."
        formRequirement = "replace the broken radiator."
        reqCode = "badRad"
        carRadiator = "Broken radiator"
        rand = 0
        
    if rand == 6:
        requirement = "replace the headlight."
        formRequirement = "replace the broken headlight."
        reqCode = "smashedHeadlamp"
        rand = random.randint(1,2)
        if rand == 1:
            carHeadlight1 = "None"
        if rand == 2:
            carHeadlight2 = "None"
        rand = 0

    if rand == 7:
        requirement = "replace the tail light."
        formRequirement = "replace the broken tail light."
        reqCode = "smashedTailLamp"
        rand = random.randint(1,2)
        if rand == 1:
            carTailLight1 = "None"
        if rand == 2:
            carTailLight2 = "None"
        rand = 0
            
    if rand == 8:
        requirement = "fix the engine."
        formRequirement = "replace the broken engine."
        reqCode = "bustEngine"
        carEngine = "Busted engine"
        rand = random.randint(1,10)
        if rand == 1:
            rollUp = "is towed into"
        if rand != 1:
            rollUp = "is pushed into"
        rand = 0
            
    if rand == 9:
        requirement = "replace the transmission."
        formRequirement = "replace the broken transmission."
        reqCode = "badTransmission"
        carTransmission = "Broken transmission"
        
    if rand == 10:
        requirement = "replace the leaking fuel tank."
        formRequirement = "replace the punctured fuel tank."
        reqCode = "leaker"
        carFuelTank = "Punctured fuel tank"
        rand = random.randint(1,10)
        if rand == 1:
            rollUp = "is towed into"
        if rand != 1:
            rollUp = "is pushed into"
        rand = 0

    if rand == 11:
        requirement = "replace the broken radio."
        formRequirement = "replace the broken radio."
        reqCode = "badRadio"
        carRadio = "Broken radio"
        rand = 0

    changeCarGraphics()
    updateTime()

    print("\n  A car " + rollUp + " the garage.")
    time.sleep(2)
    print("\n  It is a")

    print("  " + carName + "\n")
    print("  " + "The customer says to " + requirement + " You write this down.\n")
    print("  " + carLine1)
    print("  " + carLine2 + "       From initial inspection")
    print("  " + carLine3 + "       it appears that the car")
    print("  " + carLine4 + "       has the following parts:")
    print("  " + carLine5 + "            FL tire: " + carTire1)
    print("  " + carLine6 + "            FR tire: " + carTire2)
    print("  " + carLine7 + "            RL tire: " + carTire3)
    print("  " + carLine8 + "            RR tire: " + carTire4)
    print("  " + carLine9 + "        L headlight: " + carHeadlight1)
    print("  " + carLine10 + "        R headlight: " + carHeadlight2)
    print("  " + carLine11 + "       L tail light: " + carTailLight1)
    print("  " + carLine14 + "       R tail light: " + carTailLight2)
    print("  " + carLine15)
    print("  " + carLine16)
    print("  " + carLine17)
    print("  " + carLine18)
    print("")
    print("  " + "It is " + str(hours) + ":" + minutesStr + " on day " + str(day))
    print("  " + "You have " + str(money) + "$")

    print("\n1. Inspect the vehicle further")
    print("2. Check work order")
    print("3. Modify vehicle")
    print("4. Send vehicle off")
    plrinput = input("\n>>> ")
    plrinput = int(plrinput)
    if plrinput == 1:
        drawInspectionMenu()
    if plrinput == 2:
        checkWorkOrder()
    if plrinput == 3:
        while plrinput != 20:
            modifyCar()
    if plrinput == 4:
        checkVehicle()



#Updates display time
#Dependancies: time
#Dependants: generateWorkCar(), drawInspectionMenu()
def checkVehicle():
    #Globalizes variables
    global money
    global rand
    global minutes

    print("")
    #Finds reqCode
    if reqCode == "oneTire":
        #Finds if tires are mismatched or missing
        if carTire1 == carTire2 == carTire3 == carTire4 != "None":
            print("  The customer says thanks and leaves after paying.")
            #Adds money depending on tires used
            if carTire1 == "Economy tire":
                rand = random.randint(75, 125)
                rand = rand * tiresChanged
            if carTire1 == "Regular tire":
                rand = random.randint(125, 200)
                rand = rand * tiresChanged
            if carTire1 == "Sport tire":
                rand = random.randint(200, 350)
                rand = rand * tiresChanged
            if carTire1 == "Heavy duty tire":
                rand = random.randint(250, 425)
                rand = rand * tiresChanged
            if carTire1 == "Offroad tire":
                rand = random.randint(300, 525)
                rand = rand * tiresChanged
            if carTire1 == "Bulletproof tire":
                rand = random.randint(400, 700)
                rand = rand * tiresChanged
        #Checks if tires are missing
        if carTire1 == "None" or carTire2 == "None" or carTire3 == "None" or carTire4 == "None":
            rand = 0
            print("  The customer says that there are still missing tires,\n  and they leave without paying.")
        else:
            #Checks if tires are mismatched.
            if carTire1 != carTire2 or carTire2 != carTire3 or carTire3 != carTire4 or carTire1 != carTire4:
                print("  The customer says the tires are mismatched,\n  and they leave after paying half price.")

    if reqCode == "twoTires":
        if carTire1 == carTire2 == carTire3 == carTire4 != "None":
            print("  The customer says thanks and leaves after paying.")
            if carTire1 == "Economy tire":
                rand = random.randint(75, 125)
                rand = rand * tiresChanged
            if carTire1 == "Regular tire":
                rand = random.randint(125, 200)
                rand = rand * tiresChanged
            if carTire1 == "Sport tire":
                rand = random.randint(200, 350)
                rand = rand * tiresChanged
            if carTire1 == "Heavy duty tire":
                rand = random.randint(250, 425)
                rand = rand * tiresChanged
            if carTire1 == "Offroad tire":
                rand = random.randint(300, 525)
                rand = rand * tiresChanged
            if carTire1 == "Bulletproof tire":
                rand = random.randint(400, 700)
                rand = rand * tiresChanged
        if carTire1 == "None" or carTire2 == "None" or carTire3 == "None" or carTire4 == "None":
            rand = 0
            print("  The customer says that there are still missing tires,\n  and they leave without paying.")
        else:
            if carTire1 != carTire2 or carTire2 != carTire3 or carTire3 != carTire4 or carTire1 != carTire4:
                print("  The customer says the tires are mismatched,\n  and they leave after paying half price.")

    if reqCode == "battery":
        if carBattery != "None" and carBattery != "Dead battery":
            print("  The customer says thanks and leaves after paying.")
            if carBattery == "Economy battery":
                rand = random.randint(100, 200)
            if carBattery == "Low charge battery":
                rand = random.randint(150, 275)
            if carBattery == "Regular battery":
                rand = random.randint(200, 350)
            if carBattery == "High charge battery":
                rand = random.randint(300, 500)
            if carBattery == "Heavy duty battery":
                rand = random.randint(350, 575)
        if carBattery == "None" or carBattery == "Dead battery":
            rand = 0
            print("  The customer says that the car still won't start,\n  and they leave without paying.")

    if reqCode == "cb":
        if carRadio == "CB radio":
            print("  The customer says thanks and leaves after paying.")
            rand = random.randint(325, 475)
        if carRadio != "CB radio":
            rand = 0
            print("  The customer says that the car still doesn't have a CB radio,\n  and they leave without paying.")

    if reqCode == "badRad":
        if carRadiator != "None" and carRadiator != "Broken radiator":
            print("  The customer says thanks and leaves after paying.")
            if carRadiator == "Economy radiator":
                rand = random.randint(100, 225)
            if carRadiator == "Regular radiator":
                rand = random.randint(200, 325)
            if carRadiator == "Performance radiator":
                rand = random.randint(350, 475)
            if carRadiator == "Heavy duty radiator":
                rand = random.randint(400, 650)
        if carRadiator == "None" or carRadiator == "Broken radiator":
            rand = 0
            print("  The customer says that the car still overheats,\n  and they leave without paying.")

    if reqCode == "smashedHeadlamp":
        if carHeadlight1 != "None" and carHeadlight2 != "None":
            print("  The customer says thanks and leaves after paying.")
            if carHeadlight1 == "Regular headlight":
                rand = random.randint(50, 150)
            if carHeadlight1 == "Xenon headlight":
                rand = random.randint(200, 350)
            if carHeadlight1 == "Reinforced headlight":
                rand = random.randint(250, 400)
        if carHeadlight1 == "None" or carHeadlight2 == "None":
            rand = 0
            print("  The customer says that there are still missing headlights,\n  and they leave without paying.")
        else:
            if carHeadlight1 != carHeadlight2 and carHeadlight1 != "None" and carHeadlight2 != "None":
                print("  The customer says the headlights are mismatched,\n  and they leave after paying half price.")

    if reqCode == "bustEngine":
        if carEngine != "None" and carEngine != "Busted engine":
            print("  The customer says thanks and leaves after paying.")
            if carEngine == "Low liter engine":
                rand = random.randint(150, 250)
            if carEngine == "Economy engine":
                rand = random.randint(300, 475)
            if carEngine == "Regular engine":
                rand = random.randint(500, 650)
            if carEngine == "Sport engine":
                rand = random.randint(750, 900)
            if carEngine == "Heavy duty engine":
                rand = random.randint(850, 1050)
        if carEngine == "None" or carEngine == "Busted engine":
            rand = 0
            print("  The customer says that the car still doesn't have a working engine,\n  and they leave without paying.")

    if reqCode == "badTransmission":
        if carTransmission != "None" and carTransmission != "Broken transmission":
            print("  The customer says thanks and leaves after paying.")
            if carTransmission == "Regular automatic":
                rand = random.randint(300, 450)
            if carTransmission == "Sport automatic":
                rand = random.randint(500, 675)
            if carTransmission == "Heavy duty automatic":
                rand = random.randint(600, 750)
            if carTransmission == "Regular manual":
                rand = random.randint(250, 350)
            if carTransmission == "Sport manual":
                rand = random.randint(400, 525)
            if carTransmission == "Heavy duty manual":
                rand = random.randint(500, 650)
        if carTransmission == "Broken transmission":
            rand = 0
            print("  The customer says that the car still doesn't shift right,\n  and they leave without paying.")
        if carTransmission == "None":
            rand = 0
            print("  The customer says that the gear stick doesn't do anything,\n  and they leave without paying.")

    if reqCode == "leaker":
        if carFuelTank != "None" and carFuelTank != "Punctured fuel tank":
            print("  The customer says thanks and leaves after paying.")
            if carFuelTank == "Low capacity tank":
                rand = random.randint(75, 125)
            if carFuelTank == "Normal tank":
                rand = random.randint(150, 225)
            if carFuelTank == "High capacity tank":
                rand = random.randint(300, 425)
            if carFuelTank == "Heavy duty tank":
                rand = random.randint(325, 450)
        if carFuelTank == "None" or carFuelTank == "Punctured fuel tank":
            rand = 0
            print("  The customer says that the car still leaks fuel,\n  and they leave without paying.")

    if reqCode == "badRadio":
        if carRadio != "None" and carRadio != "Broken radio":
            print("  The customer says thanks and leaves after paying.")
            if carRadio == "Commuter radio":
                rand = random.randint(150, 350)
            if carRadio == "CB radio":
                rand = random.randint(325, 550)
            if carRadio == "Military radio":
                rand = random.randint(1000, 1300)
        if carRadio == "None" or carRadio == "Broken radio":
            rand = 0
            print("  The customer says that the car still lacks a working radio,\n  and they leave without paying.")

    print("  + " + str(rand) + "$")
    print("  This is a " + str(rand - moneySpent) + "$ profit.")
    money = money + rand
        
    time.sleep(1.5)
    print("\n")
    print("  You wait a while. \n")
    minutes = minutes + random.randint(0, 180)
    time.sleep(1.5)
    generateWorkCar()



#Reads off manual
#Dependancies: none
#Dependants: modifyCar()
def checkManual(entry, read):
    #Finds entry
    if entry == "CAV_ALM1":
        #Sets entry values
        manualCarName = "1st GEN CAVICE ALMADA"
        manualCarEngine = "Economy engine"
        manualCarRadiator = "Economy radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Economy tire"
        manualCarBattery = "Economy battery"
        manualCarFuelTank = "Low capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_ALM2":
        manualCarName = "2nd GEN CAVICE ALMADA"
        manualCarEngine = "Economy engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Economy tire"
        manualCarBattery = "Economy battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_TRACER":
        manualCarName = "CAVICE TRACER"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_OMEGA":
        manualCarName = "CAVICE OMEGA"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_CAP":
        manualCarName = "CAVICE CAPACITY"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "High capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_SAT1":
        manualCarName = "1st GEN CAVICE SATELLITE"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Sport tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_SAT2":
        manualCarName = "2nd GEN CAVICE SATELLITE"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Sport tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Xenon headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_GEM":
        manualCarName = "CAVICE GEMINI"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Sport tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Xenon headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_M7":
        manualCarName = "7th GEN CAVICE M-SERIES"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Heavy duty radiator"
        manualCarTransmission = "Regular manual"
        manualCarSuspension = "Offroad suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "None"

    if entry == "CAV_M9":
        manualCarName = "9th GEN CAVICE M-SERIES"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Heavy duty radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "Offroad suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_M11":
        manualCarName = "11th GEN CAVICE M-SERIES"
        manualCarEngine = "Heavy duty engine"
        manualCarRadiator = "Heavy duty radiator"
        manualCarTransmission = "Heavy duty automatic"
        manualCarSuspension = "Heavy duty suspension"
        manualCarTire = "Heavy duty tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_MSS":
        manualCarName = "CAVICE M-SERIES SUPER SWAMPER"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "Heavy duty suspension"
        manualCarTire = "Offroad tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Xenon headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_C4":
        manualCarName = "4th GEN CAVICE C-SERIES"
        manualCarEngine = "Heavy duty engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "High capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "CB radio"

    if entry == "CAV_RO1":
        manualCarName = "1st GEN CAVICE ROAMER"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "High capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_RO2":
        manualCarName = "2nd GEN CAVICE ROAMER"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "High capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_CAM2":
        manualCarName = "2nd GEN CAVICE CAMBIO"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Sport manual"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_CAM3":
        manualCarName = "3rd GEN CAVICE CAMBIO"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "CAV_CAM4":
        manualCarName = "4th GEN CAVICE CAMBIO"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Performance radiator"
        manualCarTransmission = "Sport automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "HIL_WRE":
        manualCarName = "HIGHLANDER WRESTLER"
        manualCarEngine = "Sport engine"
        manualCarRadiator = "Heavy duty radiator"
        manualCarTransmission = "Heavy duty automatic"
        manualCarSuspension = "Offroad suspension"
        manualCarTire = "Offroad tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Xenon headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "HIL_COM1":
        manualCarName = "1st GEN HIGHLANDER COMANCHE"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "HIL_COM2":
        manualCarName = "2nd GEN HIGHLANDER COMANCHE"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "High charge battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "FOR_SCR":
        manualCarName = "FORTUNA SOCCER"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Low capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "Regular tail light"
        manualCarRadio = "Commuter radio"

    if entry == "FOR_JET":
        manualCarName = "FORTUNA JET"
        manualCarEngine = "Regular engine"
        manualCarRadiator = "Regular radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "FOR_BUG":
        manualCarName = "FORTUNA BUG"
        manualCarEngine = "Economy engine"
        manualCarRadiator = "Economy radiator"
        manualCarTransmission = "Regular automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Regular tire"
        manualCarBattery = "Economy battery"
        manualCarFuelTank = "Regular tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "RCH_500":
        manualCarName = "ROACH 500"
        manualCarEngine = "Low liter engine"
        manualCarRadiator = "Economy radiator"
        manualCarTransmission = "Regular manual"
        manualCarSuspension = "City suspension"
        manualCarTire = "Economy tire"
        manualCarBattery = "Regular battery"
        manualCarFuelTank = "Low capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    if entry == "RCH_700":
        manualCarName = "ROACH 700"
        manualCarEngine = "Low liter engine"
        manualCarRadiator = "Economy radiator"
        manualCarTransmission = "Regular Automatic"
        manualCarSuspension = "City suspension"
        manualCarTire = "Economy tire"
        manualCarBattery = "Economy battery"
        manualCarFuelTank = "Low capacity tank"
        manualCarHeadlight = "Regular headlight"
        manualCarTailLight = "LED tail light"
        manualCarRadio = "Commuter radio"

    #Checks read
    if read == 1:
        #Prints out manual
        print("  " + manualCarName + " OPERATOR'S MANUAL")
        print("  " + "      Engine: " + manualCarEngine)
        print("  " + "    Radiator: " + manualCarRadiator)
        print("  " + "Transmission: " + manualCarTransmission)
        print("  " + "  Suspension: " + manualCarSuspension)
        print("  " + "       Tires: " + manualCarTire)
        print("  " + "     Battery: " + manualCarBattery)
        print("  " + "   Fuel tank: " + manualCarFuelTank)
        print("  " + "  Headlights: " + manualCarHeadlight)
        print("  " + " Tail lights: " + manualCarTailLight)
        print("  " + "       Radio: " + manualCarRadio)

    time.sleep(4)
    #Returns flow
    drawInspectionMenu()



#Shows work order
#Dependancies: none
#Dependants: generateWorkCar(), drawInspectionMenu()
def checkWorkOrder():
    #Prints out form work order
    print("  The work order says to " + formRequirement)
    time.sleep(1.5)
    #Returns flow
    drawInspectionMenu()



#Shows full inspection menu
#Dependancies: none
#Dependants: saveProgress(), loadProgress(), modifyCar(), makeWorkOrder(), checkManual()
def drawInspectionMenu():
    changeCarGraphics()
    updateTime()

    #Prints GUI
    print("\n" + "  " + carName + "\n")
    print("  " + carLine1 + "             Engine: " + carEngine)
    print("  " + carLine2 + "           Radiator: " + carRadiator)
    print("  " + carLine3 + "       Transmission: " + carTransmission)
    print("  " + carLine4 + "      FL suspension: " + carSuspension1)
    print("  " + carLine5 + "      FR suspension: " + carSuspension2)
    print("  " + carLine6 + "      RL suspension: " + carSuspension3)
    print("  " + carLine7 + "      RR suspension: " + carSuspension4)
    print("  " + carLine8 + "            FL tire: " + carTire1)
    print("  " + carLine9 + "            FR tire: " + carTire2)
    print("  " + carLine10 + "            RL tire: " + carTire3)
    print("  " + carLine11 + "            RR tire: " + carTire4)
    print("  " + carLine12 + "            Battery: " + carBattery)
    print("  " + carLine13 + "          Fuel tank: " + carFuelTank)
    print("  " + carLine14 + "        L headlight: " + carHeadlight1)
    print("  " + carLine15 + "        R headlight: " + carHeadlight2)
    print("  " + carLine16 + "       L tail light: " + carTailLight1)
    print("  " + carLine17 + "       R tail light: " + carTailLight2)
    print("  " + carLine18 + "              Radio: " + carRadio)
    print("")
    #Prints time and money
    print("  " + "It is " + str(hours) + ":" + minutesStr + " on day " + str(day))
    print("  " + "You have " + str(money) + "$")

    print("\n" + "1. Check work order")
    print("2. Modify vehicle")
    print("3. Send vehicle off")
    print("4. Save progress")
    plrinput = input("\n>>> ")
    plrinput = int(plrinput)
    #Starts flow
    if plrinput == 1:
        checkWorkOrder()
    if plrinput == 2:
        while plrinput != 20:
            modifyCar()
    if plrinput == 3:
        checkVehicle()
    if plrinput == 4:
        saveProgress()



#Runs main
#Dependancies: none
#Dependants: main
def eventHandler():
    generateWorkCar()



if bypassIntro != 1:
    print(" ")
    time.sleep(3)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒┌─────────────────┐▒")
    print("▒│ Wasteland       │▒")
    print("▒│        Mechanic │▒")
    print("▒└─────────────────┘▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("         v0.2        ")
    print("")
    print("o _           ┌──┐    ")
    print("|\            │[]│┌──┐")
    print("          ┌──┐│[]││[]│")
    print("          │[]││[]││[]│")
    print("          │[]││[]││[]│")
    print("    ╹     ┴──┴┴──┴┴──┴")
    print("                      ")
    print("   Those Who Wander   ")
    time.sleep(3)
    print("\nWelcome to the wasteland.")
    print("\n")
    time.sleep(4)
    print("Your garage still stands, even after the bombs fell.")
    time.sleep(5)
    print("\nAs a part time mechanic, your job is to repair the vehicles brought")
    print("to you by roaming wastelanders, as well as go out and scavenge or buy")
    print("more car parts.")
    time.sleep(11)
    print("\nGood luck.")
    time.sleep(4)
print("\nWould you like to load a save?")
print("\n" + "1. Yes")
print("2. No")
plrinput = input("\n>>> ")
plrinput = int(plrinput)
if plrinput == 1:
    loadProgress()
if plrinput == 2:
    eventHandler()
