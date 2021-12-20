# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from numpy import arctan, pi, cos, sin, sqrt, divide
class House:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the house
        # orientation: orientation of the house

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]  
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0  
                
        # Objects list
        self.objects = []

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self
       
    # Adds an object    
    def add(self, x):
        self.objects.append(x)
        return self
            
    # Draws the house      
    def draw(self):  
        gl.glPushMatrix()
        gl.glRotatef(self.parameters['orientation'], 0, 0, 1)
        gl.glTranslatef(self.parameters['position'][0], self.parameters['position'][1], self.parameters['position'][2])
        ...
        
        for o in self.objects:
            x=o.parameters['position'][0]
            y=o.parameters['position'][1]

            phi = arctan(divide(y,x))*180/pi if not(x==0) else 90
            teta = o.parameters['orientation']+phi
            
            x_ = sqrt(pow(x,2)+ pow(y, 2)) * cos(teta*pi/180)
            y_ = sqrt(pow(x,2)+ pow(y, 2)) * sin(teta*pi/180)

            gl.glPushMatrix()
            gl.glTranslatef(float(x-x_), float(y-y_),0)
            o.draw()
            gl.glPopMatrix()
        gl.glPopMatrix()