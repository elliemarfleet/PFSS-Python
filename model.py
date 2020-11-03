#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:48:17 2020

@author: elliemarfleet
"""

# import all necessary libraries in addition to class framework
import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
from itertools import combinations
import csv
import requests
import bs4
import time



# read the csv 
environment = []
f = open("in.txt", newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)



# make a new list and append rows to the rowlist
# then append a rowlist to environment list (has been done in loop format)
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

f.close()



# set dimensions of environment to ensure agents won't be plotted outside grid boundaries
y_len = len(environment)
x_len = len(environment[0])



# create initial lists for agents and variables
num_of_agents = 10
agents = []
neighbourhood = 20
num_of_it = 100



# web scraping 
# get x and y data from site
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)



# make the agents 
# environment length is 300, and the scraped data is between 0 and 100
# data is therefore multiplied by 3 so agents are spread across the environment at the same scale  
# the environment list is also passed into the agent's constructor
for i in range(num_of_agents):
    y = (int(td_ys[i].text)) * 3
    x = (int(td_xs[i].text)) * 3

    if y >= y_len:
        y = y % y_len 
    if x >= x_len:
        x = x % x_len
    agents.append(agentframework.Agent(environment, agents, y, x))
    


# check agents have access to the list of agents
agents[1].x
agents[5].agents[1].x



# initialise plot
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



# move the agents
# use shuffle to randomize order showing animation of agents
def update(frame_number):
    
    fig.clear()  

    matplotlib.pyplot.imshow(environment)

    random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share(neighbourhood)

    for agent in agents:
        matplotlib.pyplot.scatter(agent.x, agent.y)


# add a function that will run the model and connect to menu
# canvas.show() incompatible with my machine so .draw() function was used
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=num_of_it, repeat=False)
    canvas.draw()
    
    

# build the main window (root)
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



# use lecture notes to create a menu and associate menu with run function
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 



# set GUI to wait for events
tkinter.mainloop()



# write total amount stored by all agents into a file
totalstore = 0
for agent in agents:
     totalstore = agent.store + totalstore
storefile = open('storefile.txt', 'a')
storefile.write('Total agent store: ' + str(totalstore) + '\n')
storefile.close()



# END OF MODEL



'''
# write out the environment as a csv file
envifile = open('envifile.txt', 'w', newline = '')
writer = csv.writer(envifile)
writer.writerows(environment)
envifile.close()
'''


# EXCESS CODE NOT VITAL FOR MODEL TO RUN BUT USEFUL IN PROVIDING ADDITIONAL INFORMATION

# you can set the random seed so you always get the same output to ensure consistency of results
# random.seed(1)

# Finding the minimum and maximum distances 
# print(distance_list)
# max(distance_list)
# min(distance_list)




