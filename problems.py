'''
This file will contain your the code for your problems. 
'''

import numpy as np
import cv2

class City:
       universities =0
       gasStations = 0
       neighborhoods = 0
       airports = 0
       hospitals = 0
       name = "Somewhereville"
       goals =  universities + gasStations + neighborhoods + hospitals + airports
       emptyNodes = goals
       #mild
       temperature = 70
       numberOfNodes = goals + emptyNodes
       goalsLeft = numberOfNodes

       #buildcity

#class Tucson(City):


#class Flagstaff(City):

#class Prescott(City):

#class Williams(City):


class Place:
    name = "Somewhere"
    demand = 0
    electromagneticStorm = False
    connectsTo = []
    nodeConectivity = connectsTo.len()
    powered = False

class Operator:
    def __init__(self):
        city  = City()
        #staticLegalMoves = [turnOn, turnOff, generateMore, generateLess, serve]
        steps = 0



    