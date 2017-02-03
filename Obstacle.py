# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 16:56:24 2017

@author: Xavier
"""

from random import randint

class Obstacle:
    
    def __init__(self, v, xStart = 300):
        
        self.xStart = xStart
        
        self.x = 0
        self.y = 0
        
        self.width = 0
        self.height = 0
        
        self.V = -abs(v)
        
        
        self.savedMoves = []
        self.moveIndex = 0
        
        self.nMoves = 1000
        
        self.createObs()

            
        self.reset()
      
        
    def createObs(self):
        self.savedMoves = []
        n = self.nMoves
        for i in range(n):
            y = 50*randint(0,3)  
            w = randint(10,50)
            h = -randint(10,50)
            
            self.savedMoves.append((y,w,h))
        
            
    def reset(self):
        self.moveIndex = 0
        self.new()

    
    def update(self):
        self.x += self.V
        
        if(self.x <0):
            self.new()
    
    def new(self):
        i = self.moveIndex
        self.moveIndex += 1
        
        y, w, h = self.savedMoves[i]
        
        self.x = self.xStart
        self.y = y
        self.width = w
        self.height = -h
        
        
        if self.moveIndex >= len(self.savedMoves):
            print 'trop fort !'
            self.moveIndex = 0
            self.createObs()
        
        
        
    def data(self):
        return [self.x, self.y, self.width, self.height, self.V]
        

    def display(self):   
        #fill(255)
        #rect(Xobs, -Yobs+height/2, tailleObs[0], tailleObs[1],90)
        
        g=0
        g=g
        
