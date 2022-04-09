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
    map = mapGen
    #Sets the minimum limit for map generation
    x = curPos - range
    #Sets maximum limit of map generation to be the end of loop
    while x < curPos + range:
        #Checks to see if tile is mapped
        if map[x] == "unmapped":
            x = random.randint(0, 100)
            if x < 80:
                #80% chance to become a plain travelable tile
                map[x] = "road"
            else:
                #20% chance to become a special building tile from places, places are handled by director
                if len(places) != 0:
                    map[x] = random.choice(places)
                    places.remove(map[x])
                else:
                    map[x] = "road"
        x = x + 1
    return map

def formatMap(map, currentPosition, locationData):
    readerPosition = 0
    formattedMap = ""
    while len(formattedMap) < len(map):
        if readerPosition == currentPosition:
            formattedMap = formattedMap + "@"
        else:
            formattedMap = formattedMap + locationData[map[readerPosition]]["character"]
        readerPosition = readerPosition + 1
    return formattedMap

        
def director(mode, needs, number, buildings, locationData):
    possiblePlaces = []
    if mode == "passive":
        if "fw" in needs:
            possiblePlaces.append("fw")
        if "parts" in needs:
            possiblePlaces.append("parts")
        if "weapons" in needs:
            possiblePlaces.append("weapons")
        if "medical" in needs:
            possiblePlaces.append("medical")
        possiblePlaces.append("other")
        possiblePlaces.append("other")
    if mode == "neutral":
        possiblePlaces.append("fw"),
        possiblePlaces.append("parts"),
        possiblePlaces.append("weapons"),
        possiblePlaces.append("medical")
        possiblePlaces.append("other")
        possiblePlaces.append("other")
    if mode == "sadistic":
        possiblePlaces.append("fw"),
        possiblePlaces.append("parts"),
        possiblePlaces.append("weapons"),
        possiblePlaces.append("medical")
        possiblePlaces.append("other")
        if "fw" in needs:
            possiblePlaces.remove("fw")
        if "parts" in needs:
            possiblePlaces.remove("parts")
        if "weapons" in needs:
            possiblePlaces.remove("weapons")
        if "medical" in needs:
            possiblePlaces.remove("medical")
    possiblePlaces.append("fw"),
    possiblePlaces.append("parts"),
    possiblePlaces.append("weapons"),
    possiblePlaces.append("medical")
    possiblePlaces.append("other")
    places = []
    findPlace = random.choice(buildings)
    while len(places) < number:
        while locationData[findPlace]["type"] not in possiblePlaces:
            findPlace = random.choice(buildings)
        places.append(findPlace)
    return places