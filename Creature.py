# -*- coding: utf-8 -*-

from Network import Network

g = -0.3

class Creature:       
    
    def __init__ (self, l, weights = 0, biases = 0):
    
        self.nInputs = l[0]
        self.nNeurons  = l[1]
        self.nOuptuts = l[2]
        #self.longueur_totale_creature = nb_Entrees*nb_NoeudsLayer1 + nb_NoeudsLayer1*nb_NoeudsLayer2 + nb_NoeudsLayer2*nb_Sorties
        
        self.x = 0
        self.y = 0
        self.V = 0
        
        if  weights == 0 and biases == 0:
            self.network = Network(l,);
        else:
            self.network = Network(l, weights, biases);
            
        
        self.fitness = 0
        self.fitnessPourcentage = 0
        
        self.vivant = True
        
        self.width = 50
        self.height = -50
        

    
    def collision(self, obs):
        if self.vivant:
            if self.x+self.width > obs.x  and self.x < obs.x+obs.width and obs.y >= self.y+obs.height and obs.y <= self.y-self.height:
                return True
        return False
    
    def update(self, obs):
        if self.y == 0:
            i = obs.data()
            answer = self.network.forward(i)  
            if answer >= 0.5:
                self.V = 10.
            
        if self.y >= 0:
            self.V += g

        self.y += self.V
    
        if(self.y < 0):
            self.y = 0
            
    def reset(self):
        self.x = 0
        self.y = 0
        self.V = 0
        
        self.fitness = 0
        self.vivant = True
        

