'''
This file will contain your the code for your problems. 
'''

import numpy as np
import cv2
import random

class City():
         def __init__(self, name, universities, hospitals, airports, neighborhoods, gasStations, temperature):
            self.universities = universities
            self.gasStations = gasStations
            self.neighborhoods = neighborhoods
            self.airports = airports
            self.hospitals = hospitals
            self.name = name
            self.temperature = temperature
            self.goals = self.gasStations + self.universities + self.neighborhoods + self.airports + self.hospitals
            self.emptyNodes = self.goals
            self.totalNumberNodes = self.goals *2
         
       #buildcity

class Place:
    def __init__(self):
      self.name = "Somewhere"
      self.demand = 0
      self.electromagneticStorm = False
      self.connectsTo = []
      #self.nodeConectivity = len(self.connectsTo)
      self.powered = False
    
#arguments for city in order for function 
# name, universities, hospitals, airports, neighborhoods, gasStations, temperature
class Operator:
    def __init__(self):
        Tucson  = City("Tucson", 1, 10, 13, 150, 275, 100)
        Flagstaff = City("Flagstaff", 1, 4, 3, 37, 40, 30)
        Prescott = City("Prescott", 2,3,1,10,20,60)
        Williams = City("Williams", 0,0,1,4,9,50)
        #self.staticLegalMoves = [turnOn, turnOff, generateMore, generateLess, serve]
        #self.steps = 0



    