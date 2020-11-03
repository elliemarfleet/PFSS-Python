# PFSS-Python
 Code for the September module Programming for Social Sciences: Core Skills in Python.
 
## Introduction
This repositary contains the final code produced for the September 2020 module "Programming for Social Scientists: Core Skills in Python". The module focused on providing a basis to the Python language, with code typically produced in Spyder (part of the Anaconda package) due to the benefits of using a cross-platform integrated development environment (IDE), as opposed to through the simplified Python shell command.

The aim of the code is to produce an Agent-Based Model (ABM); simulating the behvaiour of agents as they move around in the virtual environment - the environment cosists of data which was read in using the [in.txt](in.txt) file in this repository. The simulation of agent behaviours was achieved through an object-orientated approach due to the production of the Agent class which defines the behaviours of all instances of the agent. 

## Repository contents

**The model**

[agentframework.py](agentframework.py): this file formulates the agent class.

[model.py](model.py): this file runs the model.


If attempting to run the model, both files must exist in the same directory, and the [agentframework.py](agentframework.py) file must be imported at the top of the [model.py](model.py) file in order for the code to function correctly. Although this is included within the code, please bear this in mind if difficulties are encountered during any early stages. Generally, textual comments have been added which are signified when chunks of code are preceded by the hash key, these comments typically explain to readers what the following section of code is intended to do.

## Running the model

```
python model.py
```
When attempting to run the model, a GUI window will appear with a drop-down option in the top left corner ('Model'), which then offers the option to **'Run model'**. Please allow time for the model to run as results are not always immediate due to the geocomputation required.

Following this, you should see 20 agents plotted on a 300 x 300 environment. These agents will be randomly initialised; changing colour with each turn. The environment itself should change as the agents move around as they 'eat' (take from the environment) and are 'sick' (thus giving back to the environment). The whole process will run for 100 iterations and the results will be written to a separate file ('storefile') containing the sum of the agents' stores by the last iteration.

## License

This project has been licensed under the [MIT License](https://github.com/elliemarfleet/PFSS-Python/blob/main/LICENSE).



