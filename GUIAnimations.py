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
                  ,
       ,        ____         ______          ,
               /_  /   ,  __/|__|__\____
--------------  / /  ----|  _    `   _  |-----------
               / /       \-(_)------(_)-/
------------  /_/  ---------------------------------
  ,                ,             ,      ,
"""
    msg2 = """
  Main Menu
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

def loading(stage, top = ""):
    if stage == 0:
        if top != "":
            print(top)
        print("""
       ,  ______       ,    
   ,   __/|__|__\____    ,
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
,        ░░░░░░░░░░      ,
        """)
    if stage == 1:
        if top != "":
            print(top)
        print("""
      ,   ______      ,    ,
  ,    __/|__|__\____   ,
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         █░░░░░░░░░     ,
        """)
    if stage == 2:
        if top != "":
            print(top)
        print("""
     ,    ______     ,    , 
 ,     __/|__|__\____  , 
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         ██░░░░░░░░    , 
        """)
    if stage == 3:
        if top != "":
            print(top)
        print("""
    ,     ______    ,    ,  
,      __/|__|__\____ ,  
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         ███░░░░░░░   ,  
        """)
    if stage == 4:
        if top != "":
            print(top)
        print("""
   ,      ______   ,    ,   
       __/|__|__\____,   
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         ████░░░░░░  ,   
        """)
    if stage == 5:
        if top != "":
            print(top)
        print("""
  ,       ______  ,    ,    
       __/|__|__\____      ,
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         █████░░░░░ ,    
        """)
    if stage == 6:
        if top != "":
            print(top)
        print("""
 ,        ______ ,    ,     
       __/|__|__\____     , 
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         ██████░░░░,     
        """)
    if stage == 7:
        if top != "":
            print(top)
        print("""
,         ______,    ,      
       __/|__|__\____    ,  
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         ███████░░░      
        """)
    if stage == 8:
        if top != "":
            print(top)
        print("""
          ______    ,       
       __/|__|__\____   ,   
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         ████████░░        ,
        """)
    if stage == 9:
        if top != "":
            print(top)
        print("""
          ______   ,        
       __/|__|__\____  ,    
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         █████████░       , 
        """)
    if stage == 10:
        if top != "":
            print(top)
        print("""
          ______  ,         
       __/|__|__\____ ,     
------|  _    `   _  |------
      \-(_)------(_)-/
----------------------------
         ██████████      ,  
        """)