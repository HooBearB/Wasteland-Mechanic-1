import json
import os
import MOOSERecoded as moose

def openFile(file):
    #Finds root directory of running file
    directory = os.path.dirname(__file__)
    #Gets file path to file in /json/ folder that is found in root directory
    filename = os.path.join(directory, (r'json/' + file + r'.json'))
    #Attempts to find file in /json/ folder found in root directory
    try:
        items = json.load(open(filename, "r"))
    #Print error message if failure is inevitably encountered
    except:
        print(moose.format.red + moose.format.bold + "Error: Could not find json file at " + filename + " using JSONHandler.py" + moose.format.end)
        items = "None"
    #Returns JSON content within file
    return items

def tryGrab(root, find, setTo):
    try:
        x = root[find]
    except:
        x = setTo
    return x