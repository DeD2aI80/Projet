# -*- coding: utf-8 -*-

from Creature import Creature
from Obstacle import Obstacle

from random import randint, random

import numpy as np


width = 1000
height = 500


class Population:
    
    def __init__(self, nCreature, layers, prob = 0.5, mutation = 0):
        
        self.population = []

        self.generation = 0
        self.prob = prob
        
        self.fitness = 0
        self.stillAlive = 0
        
        self.maxFitness = []
        
        self.obs = Obstacle(3)
        
        self.layers = layers
        self.mutation = mutation
        
        #Crée les créatures :
        for i in range(nCreature):
            c = Creature(layers)
            self.population.append(c)
        
    
    def doGeneration(self):
        self.obs.reset()
        self.resetCreatures()
        self.fitness = 0
        self.stillAlive = len(self.population)
        
        while self.stillAlive > 0:
            self.fitness += 1
            self.update()
            #print self.stillAlive, self.fitness, self.population[0].x, self.population[0].y
        
        m = self.getMaxFitness()
        self.maxFitness.append(m)
        
        self.selection()
        
        self.generation += 1
        
    
    def update(self):
        self.obs.update()
        self.updateCreatures()
        self.collision()
        
    
    def collision(self):
        for c in self.population:
            if c.collision(self.obs):   
                c.fitness = self.fitness
                c.vivant = False
                self.stillAlive-=1
    
                
    def resetCreatures(self):
        for c in self.population:
            c.reset()
            
    def updateCreatures(self):
        for c in self.population:
            if c.vivant:
                c.update(self.obs)
                
    def getMaxFitness(self):
        m=0
        for c in self.population:
            m = max(c.fitness, m)
        return m
                
    def selection(self):
        p = self.prob
        nCreatures = len(self.population)
        nBest = int(nCreatures * p)
        
        bestC = self.getBestCreatures(nBest)
        
        nNew = nCreatures-nBest
        mixCreatures = self.generateCreatures(nNew, bestC[:])
        
        self.population = bestC[:] + mixCreatures[:]

        
        
        
        


 
        
        
        
    def getBestCreatures(self, nBest):
        
        #Associe le fitness de chaque créature à sa position dans self.population 
        bestCi = [(i, self.population[i].fitness) for i in range(len(self.population)) ]
        
        #Trie la liste par fitness
        bestCi.sort(compare)
        
        #Garde les nBest créatures
        bestCi = bestCi[:nBest]
        
        #Récupère les créatures:
        bestC = [self.population[i[0]] for i in bestCi]
        
        return bestC
        
    
    def generateCreatures(self, n, pop): # pop: [(i, fitness) , ...]
        
        # Fitness permet aux créatures d'avoir plus ou moins de chance d'être choisi 
        # (à ajouter)
        # sumFitness = sum([c.fitness for c in pop])
 
        mixCreatures = []
        for i in range(n):
            a = randint(0,len(pop)-1)
            b = randint(0,len(pop)-1)
            
            #a = self.choose(pop, sumFitness)
            
            c = self.mixCreatures(pop[a], pop[b])
            mixCreatures.append(c)
        
        return mixCreatures
          
    
    def mixCreatures(self, a, b):
        
        wa = a.network.weights
        wb = b.network.weights
        
        ba = a.network.biases
        bb = b.network.biases
        
        weights = [(w1,w2) for w1, w2 in zip(wa,wb)]
        biases = [(b1,b2) for b1, b2 in zip(ba,bb)]

        newWeights = []
        newBiases = []
        
        for i in range(2):  #Parcours les couches
            layer_weights = [(w1,w2) for w1, w2 in zip(weights[i][0], weights[i][1])]

            layer_biases = [(b1,b2) for b1, b2 in zip(biases[i][0], biases[i][1])]

            newArray = []
            for w in layer_weights: #Colonne
                #print w
                newLine = []
                for i in range(len(w[0])):
                    if random()>self.mutation:
                        r = randint(0,1)  #Choisie la source du poids
                        newLine.append(w[r][i])
                    else:
                        #print 'mutW'
                        newLine.append(random())
                    
                newArray.append(newLine)
            
            newWeights.append(np.array(newArray))
            
            newArray = []
            for b in layer_biases:
                newLine = []
                for i in range(len(b[0])):
                    if random()>self.mutation:
                        r = randint(0,1)  #Choisie la source du poids
                        newLine.append(b[r][i])
                    else:
                        #print 'mutB'
                        newLine.append(random())
                    
                newArray.append(newLine)
            
            newBiases.append(np.array(newArray))
            

        c = Creature(self.layers, weights = newWeights, biases = newBiases)
         
        return c

        
    def display(self):
        for c in self.population:
            if c.vivant == True:
                #rect(c.X, -c.Y + height/2, c.width, c.height)
                h=0
                
                
def compare(i,j):
    k=j[1]-i[1]
    if k<0:
        return -1
    if k>0:
        return 1
    return 0

                