import json
import os

def openFile(file):
    #Finds root directory of running file
    directory = os.path.dirname(__file__)
    #Attempts to find file in /json/ folder found in root directory
    try:
        filename = os.path.join(directory, (r'json/' + file + r'.json'))
    #Print error message if failure is inevitably encountered
    except:
        print("\u001b[1m \u001b[31m" + "Error: Could not find json file using JSONHandler.py")
    #Returns JSON content within file
    items = json.load(open(filename, "r"))
    return items