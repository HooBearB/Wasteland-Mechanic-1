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