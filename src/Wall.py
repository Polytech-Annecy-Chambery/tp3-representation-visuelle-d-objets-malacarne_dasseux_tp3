# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
from copy import copy, deepcopy
import OpenGL.GL as gl
from Opening import Opening
from Section import Section

import math

class Wall:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5]
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False     
            
        # Objects list
        self.objects = []

        # Adds a Section for this object
        self.parentSection = Section({'width': self.parameters['width'], \
                                        'height': self.parameters['height'], \
                                        'thickness': self.parameters['thickness'], \
                                        'color': self.parameters['color'], \
                                        'edges' : self.parameters['edges'], \
                                        'position': self.parameters['position']})
        self.objects.append(self.parentSection) 
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self                 

    # Finds the section where the object x can be inserted
    def findSection(self, x):
        for item in enumerate(self.objects):
            if isinstance(item[1], Section) and item[1].canCreateOpening(x):
                return item
        return None
    
    # Adds an object    
    def add(self, x):
        section = self.findSection(x)

        positionRelative2Section = [
            x.parameters["position"][0] - (section[1].getParameter("position")[0]),
            x.parameters["position"][1] - (section[1].getParameter("position")[1]),
            x.parameters["position"][2] - (section[1].getParameter("position")[2]),
        ]

        relativeOpening = deepcopy(x)
        relativeOpening.setParameter("position", positionRelative2Section)
        newSections = section[1].createNewSections(relativeOpening)

        self.objects.pop(section[0])
        self.objects.append(x)
        for i in newSections:
            self.objects.append(i)
        return self
                    
    # Draws the faces
    def draw(self):
        gl.glPushMatrix()
        gl.glRotatef(self.parameters['orientation'], 0, 0, 1)
        for x in self.objects:
            x.draw()
        gl.glPopMatrix()
        