# we are going to develop a money agent based model simulation
# this allows agents with wealth units to distribute with other agents if they collide simultaneously in the system
# we need to import the mesa libraries for creating our simulation model
import mesa
import matplotlib.pyplot as plt
import seaborn as sns
# we first create the Model class
class Money_model(mesa.Model): #this class inherits from the superior mesa.Model class
    # model activities i.e: the number of the agents, creating the grid for agent movement and placing the agents on
    #the grid created
    def __init__(self, N, width, height): # this is a constructor class specifically for carrying out the model activities
        super().__init__() # this finishes the inheritance from the mesa.Model superior class
        self.num_of_agents = N # this is for the number of agents to be created for each model
        # now we need to create the grid for the agents movement  using the mesa spaces
        self.grid = mesa.space.MultiGrid(width,height,torus = True) # this creates the grid for the agents movement
        # creating the agents for each model
        for  i in range(self.num_of_agents):
            a = Money_agent(i, self)

            # creating the Grid axes
            x = self.random.randrange(self.grid.width) # this is the x-axis of the grid created
            y = self.random.randrange(self.grid.height) # this is the y-axis of the grid created
            # after creating the axes we place the agents on this grid
            self.grid.place_agent(a, pos = (x,y)) # this places the agents on the grid created

            # we need to shuffle the agents using the step method of the model class
    def step(self):
        self.agents.shuffle_do("step")
        #this shuffles through all the agents anonymously
# this Agent class is responsible for classifying agents under their responsible models
# movement of the agents, Agents task(transfer of wealth) and also the step method for the overall agent functionality
class Money_agent(mesa.Agent):
    def __init__(self, unique_id, model): # constructor class that constructs agents for their respective activities
        super().__init__(model) # inherits the model constructor from the mesa.Agent super class
        self.wealth = 1  # each agent has one unit of wealth initially

    def move(self): # this is for the agents' movement
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore = True, include_center = False)
        # this checks the agents neighborhood to find the possible cells it can move to
        new_position = self.random.choice(possible_steps) # this chooses the cell randomly
        self.model.grid.move_agent(self,new_position) # this moves the agent to the new cell

    def give_money(self): # this is the agent task
        cellmates = self.model.grid.get_cell_list_contents([self.pos]) # check for other cellmates for the agent
        if len(cellmates) > 1: # check if there is more than one agent in the cell
            other = self.random.choice(cellmates) # choose one agent at random
            if other != self:
                other.wealth += 1
                self.wealth -= 1

    def step(self): # this is for functionality
        self.move() # first move the agents
        if self.wealth > 0:
            self.give_money()





#implementation of our model

model = Money_model(100,60,60)

for i in range(200): # we run the model in x steps
    print(f"Step {i}")
    model.step()


#to plot a graph for the simulations' agents' wealth
#we need to import seaborn and matplotlib libraries
# we need to create a list for storing the agents wealths

wealths = [] # list for storing the agents' wealth
for agent in model.agents: # for each agent in the model created
    wealths.append(agent.wealth)

# we use the created list of agent wealths to create a graph

plt.figure(figsize = (10,10)) # this is for the size of the graph
sns.histplot(wealths, bins =range(max(wealths)+2), kde = True, stat = "count", discrete = True, edgecolor = "black")
plt.title("WEALTH DISTRIBUTION AMONG AGENTS") #title of the graph
plt.xlabel("WEALTH") # x-axis label
plt.ylabel("NUMBER OF AGENTS") # y-axis label
plt.grid(True, alpha = 0.3) # grid of the graph
plt.show() # to show the graph









