import MOOSERecoded as moose
import random



def determineMaxSpeed(hp, weight):
    return round((300 * hp ** (1/3)) / (weight ** (1/3)), 0)