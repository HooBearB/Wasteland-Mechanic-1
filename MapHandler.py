import random
import MOOSERecoded as moose

def startGen(leng):
    #Starts map list
    mapGen = []
    #Determines start as garage
    mapGen.append("garage")
    x = 0
    #Leaves empty, unmapped tiles between garage and objective
    while x < leng:
        mapGen.append("unmapped")
        x = x + 1
    #Determines end as objective
    mapGen.append("objective")
    return mapGen

def revealGen(mapGen, curPos, places, range = 2):
    #Sets the minimum limit for map generation
    x = curPos - range
    #Sets maximum limit of map generation to be the end of loop
    while x < curPos + range:
        #Checks to see if tile is mapped
        if mapGen[x] == "unmapped":
            x = random.randint(0, 100)
            if x < 80:
                #80% chance to become a plain travelable tile
                mapGen[x] = "road"
            else:
                #20% chance to become a special building tile from places, places are handled by main program director
                mapGen[x] = random.choice(places)
        x = x + 1