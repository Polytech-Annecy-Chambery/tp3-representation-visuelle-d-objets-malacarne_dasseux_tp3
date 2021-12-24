# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""

import OpenGL.GL as gl

class Opening:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: mandatory
        # width: mandatory
        # height: mandatory
        # thickness: mandatory
        # color: mandatory        

        # Sets the parameters
        self.parameters = parameters

        # Sets the default parameters 
        if 'position' not in self.parameters:
            raise Exception('Parameter "position" required.')       
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')
        if 'thickness' not in self.parameters:
            raise Exception('Parameter "thickness" required.')    
        if 'color' not in self.parameters:
            raise Exception('Parameter "color" required.')  
            
        # Generates the opening from parameters
        self.generate()  

    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self        

    # Defines the vertices and faces        
    def generate(self):
        self.vertices = [
                [0,0,0], 
                [0, 0, self.parameters['height']], 
                [self.parameters['width'], 0, self.parameters['height']],
                [self.parameters['width'], 0, 0],
                
                [0, self.parameters['thickness'], 0 ], 
                [0, self.parameters['thickness'], self.parameters['height']], 
                [self.parameters['width'],  self.parameters['thickness'], self.parameters['height']],
                [self.parameters['width'],  self.parameters['thickness'], 0]
                ]
        self.faces = [
                [0, 1, 5, 4],
                [0, 3, 7, 4],
                [1, 2, 6, 5],
                [3, 2, 6, 7]
                ]   

    # Draws the edges
    def drawEdges(self):
        lines = []
        for x in self.faces : 
            for i in range(len(x)):
                lines.append([x[i], x[i+1 if i+1 < len(x) else 0]])
                
        for l in lines : 
            gl.glBegin(gl.GL_LINES)
            gl.glColor3fv([0,0,0])
            for sommet in l : 
                gl.glVertex3fv(self.vertices[sommet])
            gl.glEnd() 

    # Draws the faces                
    def draw(self):        
        gl.glPushMatrix()
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        gl.glTranslatef(
            self.parameters['position'][0], 
            self.parameters['position'][1], 
            self.parameters['position'][2]
        )
        for f in self.faces:
            gl.glBegin(gl.GL_QUADS)
            gl.glColor3fv(self.parameters['color'])
            for sommet in f : 
                gl.glVertex3fv(self.vertices[sommet])
            gl.glEnd()
        self.drawEdges()
        gl.glPopMatrix()