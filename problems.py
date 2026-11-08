'''
This file will contain your the code for your problems. 
'''

import numpy as np
import cv2

class City():
         universities =0
         gasStations = 0
         neighborhoods = 0
         airports = 0
         hospitals = 0
         name = "Somewhereville"
         #mild
         temperature = 70
         def goals(self):
               goals = self.gasStations + self.universities + self.neighborhoods + self.airports + self.hospitals
               return goals
         def emptyNodes(self):
              return self.goals()       
         def totalNumberNodes(self):
              return self.goals() * 2

       #buildcity

class Tucson(City):
     #I am not counting community colleges, just the U of A
     name = "Tucson"
     universities = 1
     hospitals = 10
     neighborhoods = 150
     airports = 13
     gasStations = 275


class Flagstaff(City):
     name = "Flagstaff"
     universities = 1
     hospitals = 4
     neighborhoods = 37
     airports = 3
     gasStations = 40
     
class Prescott(City):
     name = "Prescott"
     universities = 2
     hospitals = 2
     neighborhoods = 10
     airports = 1
     gasStations = 20
     
class Williams(City):
      name = "Williams"
      universities = 0
      hospitals = 0
      neighborhoods = 4
      airports = 1
      gasStations = 9


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

    