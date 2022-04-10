import os
import json

print("")
directory = os.path.dirname(__file__)
print(directory)
newdirectory = os.path.dirname(directory)
print(newdirectory)
filename = newdirectory + r'/json/vehicles.json'
print(filename)
try:
    items = json.load(open(filename, "r"))
except:
    print("vehicles json not found")
    items = "None"

