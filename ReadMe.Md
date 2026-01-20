PREDATOR-PREY ECOSYSTEM SIMULATION

PROJECT DESCRIPTION

This project is a Python-based ecosystem simulation that models a predator–prey relationship using agent-based modeling. The simulation focuses on interactions between predators and prey based on energy and life units, and how these interactions influence the ecosystem over time.

The model is implemented using the Mesa library and follows Python Object-Oriented Programming (OOP) principles. Simulation results are visualized using histogram graphs.

MODEL DESCRIPTION

PREY AGENTS

Each prey has a defined number of life units.

When a predator feeds on a prey, the prey loses life units.

When the life units of a prey reach zero, the prey dies and is removed from the simulation.

PREDATOR AGENTS

Each predator has a defined number of energy units.

When a predator encounters a prey, it feeds on the prey and gains energy units.

Predator energy changes are tracked throughout the simulation.

SIMULATION PROCESS

The simulation runs in discrete time steps.

At each step, agents move and interact within the environment.

Predator–prey encounters result in energy transfer and life reduction.

Dead prey agents are removed from the model.

VISUALIZATION PROCEDURE

Simulation steps are visualized using histogram graphs.

Histograms show the distribution of prey life units and predator energy units over time.

Visualization is implemented using Matplotlib and Seaborn

TECHNOLOGIES USED

Python

Mesa (agent-based modeling framework)

Matplotlib (data visualization)

Seaborn (statistical visualization)

SOFTWARE DESIGN

The project follows Python Object-Oriented Programming principles.

Agents are implemented as classes with clearly defined behaviors.

The model, agents, and visualization logic are separated for clarity and maintainability.

PURPOSE OF THE PROJECT

The purpose of this project is to demonstrate:

Predator–prey ecosystem dynamics

Agent-based modeling using Mesa

Practical application of Object-Oriented Programming in Python

Data visualization of simulation behavior

AUTHOR AND PROGRAMMER

SSEKAMATE SHARIF

Python | Agent-Based Modeling | Ecosystem Simulation