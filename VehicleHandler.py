import MOOSERecoded as moose
import random

def loadCar(car, carJSON, itemJSON):
    object = {}
    object["id"] = car
    object["name"] = carJSON[car]["name"]
    object["display"] = carJSON[car]["display"]
    object["sidedisplay"] = carJSON[car]["sidedisplay"]

    object["engine"] = carJSON[car]["engine"]
    object["engineHealth"] = itemJSON[carJSON[car]["engine"]]["condition"]

    object["fuel_tank"] = carJSON[car]["fuel_tank"]
    object["fuelTankHealth"] = itemJSON[carJSON[car]["fuel_tank"]]["condition"]

    object["radiator"] = carJSON[car]["radiator"]
    object["radiatorHealth"] = itemJSON[carJSON[car]["radiator"]]["condition"]

    object["battery"] = carJSON[car]["battery"]
    object["batteryHealth"] = itemJSON[carJSON[car]["battery"]]["condition"]

    object["transmission"] = carJSON[car]["transmission"]
    object["transmissionHealth"] = itemJSON[carJSON[car]["transmission"]]["condition"]

    object["suspension"] = []
    while len(object["suspension"]) < carJSON[car]["numHubs"]:
        object["suspension"].append(carJSON[car]["suspension"])

    object["tires"] = []
    while len(object["tires"]) < carJSON[car]["numHubs"]:
        object["tires"].append(carJSON[car]["tires"])
    while len(object["frontlightsHealth"]) < carJSON[car]["numFrontLights"]:
        object["frontlightsHealth"].append(itemJSON[carJSON[car]["headlights"]]["condition"])

    object["frontlights"] = []
    while len(object["frontlights"]) < carJSON[car]["numFrontLights"]:
        object["frontlights"].append(carJSON[car]["headlights"])
    object["frontlightsHealth"] = []
    while len(object["frontlightsHealth"]) < carJSON[car]["numFrontLights"]:
        object["frontlightsHealth"].append(itemJSON[carJSON[car]["headlights"]]["condition"])

    object["backlights"] = []
    while len(object["backlights"]) < carJSON[car]["numBackLights"]:
        object["backlights"].append(carJSON[car]["taillights"])
    object["backlightsHealth"] = []
    while len(object["backlightsHealth"]) < carJSON[car]["numBackLights"]:
        object["backlightsHealth"].append(itemJSON[carJSON[car]["taillights"]]["condition"])

    object["radio"] = carJSON[car]["radio"]
    object["radioHealth"] = itemJSON[carJSON[car]["radio"]]["condition"]
    
    return object