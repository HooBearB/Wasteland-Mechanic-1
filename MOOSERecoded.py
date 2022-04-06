"""
   _____________  ________  ________  _________  _________
  /  __   __   / /  __   / /  __   / /  ______/ /  ______/
 /  / /  / /  / /  /_/  / /  /_/  / /______  / /  ______/
/__/ /__/ /__/ /_______/ /_______/ /________/ /________/
    ____                      __         __
   / __ \___  _________  ____/ /__  ____/ /
  / /_/ / _ \/ ___/ __ \/ __  / _ \/ __  /
 / _  _/  __/ /__/ /_/ / /_/ /  __/ /_/ /
/_/ |_|\___/\___/\____/\____/\___/\____/
"""
#v0.1
#Created by: Flint
#Maintained and added to by: (Insert the name of the guy I'm gonna bribe into looking at my shitty code)

import time

class format:
    mode = "Colour"
    clear = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    strikethrough = "\u001b[29m"
    underline = "\u001b[4m"
    italic = "\u001b[3m"
    bold = "\u001b[1m"
    dim = "\u001b[2m"
    red = "\u001b[31m"
    magenta = "\u001b[35m"
    blue = "\u001b[36m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    end = "\u001b[0m"

def displayLogo():
    print(format.clear)
    time.sleep(1)
    print(format.dim)
    print("""
MADE WITH
   _____________  ________  ________  _________  _________
  /  __   __   / /  __   / /  __   / /  ______/ /  ______/
 /  / /  / /  / /  /_/  / /  /_/  / /______  / /  ______/
/__/ /__/ /__/ /_______/ /_______/ /________/ /________/
    ____                      __         __
   / __ \___  _________  ____/ /__  ____/ /
  / /_/ / _ \/ ___/ __ \/ __  / _ \/ __  /
 / _  _/  __/ /__/ /_/ / /_/ /  __/ /_/ /
/_/ |_|\___/\___/\____/\____/\___/\____/

v0.1
""")
    time.sleep(0.1)
    print(format.clear)
    print(format.end)
    print("""
MADE WITH
   _____________  ________  ________  _________  _________
  /  __   __   / /  __   / /  __   / /  ______/ /  ______/
 /  / /  / /  / /  /_/  / /  /_/  / /______  / /  ______/
/__/ /__/ /__/ /_______/ /_______/ /________/ /________/
    ____                      __         __
   / __ \___  _________  ____/ /__  ____/ /
  / /_/ / _ \/ ___/ __ \/ __  / _ \/ __  /
 / _  _/  __/ /__/ /_/ / /_/ /  __/ /_/ /
/_/ |_|\___/\___/\____/\____/\___/\____/

v0.1
""")
    time.sleep(3)
    print(format.clear)
    print(format.dim)
    print("""
MADE WITH
   _____________  ________  ________  _________  _________
  /  __   __   / /  __   / /  __   / /  ______/ /  ______/
 /  / /  / /  / /  /_/  / /  /_/  / /______  / /  ______/
/__/ /__/ /__/ /_______/ /_______/ /________/ /________/
    ____                      __         __
   / __ \___  _________  ____/ /__  ____/ /
  / /_/ / _ \/ ___/ __ \/ __  / _ \/ __  /
 / _  _/  __/ /__/ /_/ / /_/ /  __/ /_/ /
/_/ |_|\___/\___/\____/\____/\___/\____/

v0.1
""")
    time.sleep(0.1)
    print(format.end)
    print(format.clear)

def ansiTest():
    print(format.strikethrough + "Strikethrough" + format.end)
    print(format.italic + "Italic" + format.end)
    print(format.bold + "Bold" + format.end)
    print(format.dim + "Dimmed" + format.end)
    print(format.red + "Red" + format.end)
    print(format.magenta + "Magenta" + format.end)
    print(format.blue + "Blue" + format.end)
    print(format.green + "Green" + format.end)
    print(format.yellow + "Yellow" + format.end)

def scrollingText(message, indent = 2, delay = 0.02):
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    run = 0
    while run < len(message):
        print(message[run : run + 1], end = "")
        time.sleep(delay)
        run = run + 1
    print("")

def askOption(message, options, indent = 2, delay = 0.02, lookingFor = ""):
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    print(message)
    runline = 0
    while runline < len(options):
        if runline == lookingFor:
            print("  - ", end = "")
        else:
            run = 0
            while run <= indent + 1:
                print(" ", end = "")
                run = run + 1
        print(str(runline + 1) + ". " + options[runline])
        time.sleep(delay)
        runline = runline + 1
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    decision = input("> ")
    while type(decision) != int:
        try:
            decision = int(decision)
        except:
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            print("Invalid input!")
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            decision = input("> ")
    while decision < 1 or decision > len(options):
        run = 0
        while run <= indent:
            print(" ", end = "")
            run = run + 1
        print("Invalid input!")
        run = 0
        while run <= indent:
            print(" ", end = "")
            run = run + 1
        decision = input("> ")
        while type(decision) != int:
            try:
                decision = int(decision)
            except:
                run = 0
                while run <= indent:
                    print(" ", end = "")
                    run = run + 1
                print("Invalid input!")
                run = 0
                while run <= indent:
                    print(" ", end = "")
                    run = run + 1
                decision = input("> ")
    return decision

def askOpen(message, indent = 2):
    run = 0
    while run < indent:
        print(" ", end = "")
        run = run + 1
    print(message)
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    decision = input("> ")
    while type(decision) != int:
        try:
            decision = int(decision)
        except:
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            print("Invalid input!")
            run = 0
            while run <= indent:
                print(" ", end = "")
                run = run + 1
            decision = input("> ")
    return decision

def askString(message, indent = 2):
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    print(message)
    run = 0
    while run <= indent:
        print(" ", end = "")
        run = run + 1
    decision = input("> ")
    return decision

def askToContinue():
    x = input("  Press " + format.bold + "enter" + format.end + " to continue.   ")
    print(format.clear)

