import MOOSERecoded as moose
import json
import os

def openInventory(object, inventory, items):
    #Opens list for display names of items in inventory
    dispInv = []
    x = 0
    #Adds name objects to display list
    while x < len(inventory):
        dispInv = items[dispInv[x]]["name"]
        x = x + 1
    #Uses MOOSE to ask player for item to view
    decision = moose.askOption(object, dispInv)

def determineNeeds(hunger, thirst, characterHealth, carHealth = 100):
    needs = []
    if hunger <= 25 or thirst <= 25:
        needs.append("fw")
    if characterHealth <= 50:
        needs.append("medical")
        needs.append("weapons")
        needs.append("fw")
    if carHealth <= 75:
        needs.append("parts")