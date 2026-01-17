# we are  creating an ecosystem  with preys and predators and preys get fed on by the predators
# so the agents are the preys and predators and the model that entails all the agents is the World
# we first define the agent and model classes
# we need to first import mesa library
import mesa
import matplotlib.pyplot as plt
import seaborn as sns
class World_model(mesa.Model): #this is the model that entails all the agents
    def __init__(self, X, Y, width,height): # number of preys and predators and also creating the grid for the movement of the agents
        super().__init__() # this completes the inheritance
        # generate the number of agents (preys and predators)
        self.Num_of_preys = X # the number of prey agents
        self.Num_of_predators = Y # the number of predator agents
        # create the grid for the movement of the agents using mesa spaces
        self.grid = mesa.space.MultiGrid(width,height,torus = True)

        # after creating the grid then we create the agents (preys)
        for i in range(self.Num_of_preys):
            a = Prey_Agents(i,self)

            #we create the x and y axes for our grid for agent movement
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            # we place the agents on the grid
            self.grid.place_agent(a,(x,y))


        # then we create the predator agents
        for j in range(self.Num_of_predators):
            b = Predator_Agents(j,self)
            # we then create the x and y axes
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            # then we place the agents
            self.grid.place_agent(b,(x,y))

        #then we do the shuffling of the agents
    def step(self):
        self.agents.shuffle_do("step")
class Prey_Agents(mesa.Agent): # this is the agent class that determines the prey character
    def __init__(self, unique_id, model):
        super().__init__(model) # this completes the inheritance from the mesa.Agent super class
        # initially each prey has fifty units of life
        self.life = 50
    # we then define the movement of our prey agents
    def move_prey(self): # moves the prey
        possible_step = self.model.grid.get_neighborhood(self.pos, moore = True, include_center= False) # gets the possible neighborhood of the agent
        new_pos = self.random.choice(possible_step) # this chooses a cell at random

        # moving the agent on the grid
        self.model.grid.move_agent(self, new_pos)

        # we do the agents task now
    def be_eaten(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos]) # check for other cellmates
        if len(cellmates) > 1:
            other = self.random.choice(cellmates) # get a random cellmate for the agents
            if other != self: # check if the agents is not equal to itself
                if isinstance(other, Predator_Agents): # then check if it's a predator
                    if self.life > 0:
                        self.life -= 5

                     # if the prey meets a predator it gets eaten, and it loses its life to the predator
    def death(self):
        if self.life <= 0:
            self.remove()


    # then we define the step method for this agent class
    def step(self):
        self.move_prey()
        # first move the prey across the grid
        # the prey dies if it loses all its life
        if self.life <= 0:
            self.death()
        if self.life > 0:
            self.be_eaten()



# then define the predator agents class
class Predator_Agents(mesa.Agent): # this is a class for the predators agents
    def __init__(self, unique_id, model):
        super().__init__(model)
        self.energy = 5  # each predator has five units of energy

    # we define the movement pattern of the predator agents
    def move_predator(self):
        possible = self.model.grid.get_neighborhood(self.pos, moore = True , include_center = False ) # get the possible neighborhood of the agents
        new_position = self.random.choice(possible) # choose the neighborhood randomly

        # then move the predator to the new position chosen randomly
        self.model.grid.move_agent(self, new_position )

    # we do the agents task (eating the prey it finds in its new location)
    def eat(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos]) # get cellmates in the new cell
        if len(cellmates) > 1: # check if it has any cellmates in the cell it moved to
            other = self.random.choice(cellmates) # pick a cellmate at random
            if other != self:
                if isinstance(other, Prey_Agents): # check if it encounters the prey and it feeds on it
                    self.energy += 5
                    # it gets five units of energy per prey that it feeds on


    # then  we define the step method for the predator agents functionality
    def step(self):
        self.move_predator()
        self.eat()
        if self.energy < 0:
            self.remove()


#implementation of our code

model = World_model(100,50,50,50)

for i in range(50):
    print(f"step {i}")
    model.step()

# creating a histogram for the preys life
# create a list for the preys' lives
lives = []
for prey in model.agents:
    if isinstance(prey, Prey_Agents): # check if it's a prey agent
        lives.append(prey.life)
if lives:
    plt.figure(figsize=(10, 10))
    sns.histplot(lives, kde=True, bins=range(max(lives) + 2), stat="count", discrete=True, edgecolor="black")
    plt.title("DISTRIBUTION OF PREY LIVES")
    plt.xlabel("LIVES")
    plt.ylabel("NUMBER OF PREYS")
    plt.grid(True, alpha=0.5)
    plt.show()
else:
    print("No live prey agents found")
# create a graph for the predator energies

energies = []
for agent in model.agents:
    if isinstance(agent, Predator_Agents):
        energies.append(agent.energy)

if energies:
    plt.figure(figsize=(10, 10))
    sns.histplot(energies, kde=True, bins=range(max(energies) + 2), stat="count", discrete=True, edgecolor="black")
    plt.title("DISTRIBUTION OF PREDATOR ENERGIES")
    plt.xlabel("ENERGIES")
    plt.ylabel("NUMBER OF PREDATORS")
    plt.grid(True, alpha=0.5)
    plt.show()
else:
    print("No energies found")



