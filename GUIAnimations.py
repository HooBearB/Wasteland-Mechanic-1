import MOOSERecoded as moose
import time

def mainMenu():
    msg = """
 _       __           __       __                __
| |     / /___  _____/ /____  / /___  ____  ____/ /
| | /| / / __ \/ ___/ __/ _ \/ / __ \/ __ \/ __  /
| |/ |/ / /_/ (__  ) /_/  __/ / /_/ / / / / /_/ /
|__/|__/\__/_/____/\__/\___/_/\__/_/_/ /_/\____/

           __  ___          __                _
          /  |/  /__  _____/ /_  ____  ____  (_)____
         / /|_/ / _ \/ ___/ __ \/ __ \/ __ \/ / ___/
        / /  / /  __/ /__/ / / / /_/ / / / / / /__
       /_/  /_/\___/\___/_/ /_/\__/_/_/ /_/_/\___/

                ____
               /_  /
                / /
               / /
              /_/

"""
    msg2 = """  Main Menu
    1. Start game
    2. Load game
    3. Settings
   > """
    print(moose.format.clear)
    print(moose.format.dim) 
    print(msg)
    print(msg2)
    print(moose.format.end)
    time.sleep(0.2)
    print(moose.format.clear)
    print(msg)