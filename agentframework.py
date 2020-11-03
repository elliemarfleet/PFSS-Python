#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:54:34 2020

@author: elliemarfleet
"""

# imports
import random



# create agent class and set up 2 variables for it to have (x and y)
# set up link to environment within agent class
# give agent y.max and x.max to link the maximum coordinate to environment length
class Agent:
    def __init__(self, environment, agents, y, x):
        self.y_max = len(environment) - 1
        self.x_max = len(environment[0]) - 1
        self.y = y
        self.x = x
        self.environment = environment
        self.store = 0 
        self.agents = agents
        

        
# move function: make a move method within the agent class
# agents move randomly on both axes by 1
# if they exceed the environment boundary they rejoin the other side
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.y_max
        else:
            self.y = (self.y - 1) % self.y_max 

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.x_max
        else:
            self.x = (self.x - 1) % self.x_max
            
            
            
# eat function: agents eat from the environment if the value is >10 (taking 10 from the environment and adding 10 to their store)
# if environment is <10 they add the amount remaining to their store 
# agents are sick if they eat too much and the value returns to environment (i.e. if their store is >100)            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else:
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] -= self.environment[self.y][self.x]
        
        if self.store > 100:
            self.environment[self.y][self.x] += self.store
            self.store = 0 
        
            

# share function: makes agents share by using neighbourhood value
    def share(self, neighbourhood):
        for agent in self.agents:
            if agent != self:
                distance = self.distance_between(agent)
                if distance <= neighbourhood:
                    sum = self.store + agent.store
                    average = sum/2
                    self.store = average 
                    agent.store = average 
                    print("sharing " + str(distance) + " " + str(average))
                    
                    
    
 # distance function: pythagoras code used to calculate distance
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

    def __str__(self):
        return 'Agent: ' + 'x = ' + str(self.x) + ', y = ' + str(self.y) + ', store = ' + str(self.store)

