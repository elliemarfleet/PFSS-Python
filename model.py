#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:48:17 2020

@author: elliemarfleet
"""
# imports
import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import matplotlib.animation 
import requests
import bs4
import time

# web scraping 
# get x and y data from site
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)

# read the csv
environment = []
f = open("in.txt", newline = '')
reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)

# make a new list and append rows to the rowlist
# then append a rowlist to environment list
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)

#f.close()


# you can set the random seed so you always get the same output
# random.seed(1)


# create lists for agents and variables
num_of_agents = 10
num_of_iterations = 100
agents = []
neighbourhood = 20

a = agentframework.Agent()


# use dot operator to call functions within newly created agent class
# we can get variables within this like below
a.move()
print(a.y, a.x)


# Make the agents.
# pass the environment list into the agent's constructor
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    


# check agents have access to the list of agents
agents[1].x
agents[5].agents[1].x

# initialise graph
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Move the agents.
def update(frame_number):
    
    fig.clear()  

    matplotlib.pyplot.imshow(environment)

    #for _ in range(num_of_it):
    #random.shuffle(agents)
    for agent in agents:
        agent.move()
        agent.eat()
        agent.share(neighbourhood)

    for agent in agents:
        matplotlib.pyplot.scatter(agent.x, agent.y)


# add a function that will run the model and connect to menu
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()

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



# write out the environment as a csv file
envifile = open('envifile.txt', 'w', newline = '')
writer = csv.writer(envifile)
writer.writerows(environment)
envifile.close()
