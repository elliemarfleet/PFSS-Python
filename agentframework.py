#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:54:34 2020

@author: elliemarfleet
"""

# imports
import random

# create agent class and set up 2 variables for it to have (x and y)
# we can give attributes to this
# set up link to environment within agent class
class Agent:
    def __init__(self, environment, agents, y, x):
        self.y_max = len(environment) - 1
        self.x_max = len(environment[0]) - 1
        self.y = y
        self.x = x
        self.environment = environment
        self.store = 0 
        self.agents = agents

        
        # make a move method within the agent class
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.y_max
        else:
            self.y = (self.y - 1) % self.y_max 

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.x_max
        else:
            self.x = (self.x - 1) % self.x_max
            
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
    
 # copy pythagoras code and make it a function to calculate distance
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

    def __str__(self):
        return 'Agent: ' + 'x = ' + str(self.x) + ', y = ' + str(self.y) + ', store = ' + str(self.store)

