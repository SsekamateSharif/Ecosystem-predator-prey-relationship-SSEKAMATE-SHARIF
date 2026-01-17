# we are going to create a simulation for a robotic room vacuum cleaner
# we have the Robot Agent that does the cleaning and the  room model class that we are cleaning
# we need to import our libraries that we will use
# for the graphing u need more libraries
import mesa
import matplotlib.pyplot as plt
import seaborn as sns

class Robot_Agent(mesa.Agent): # inherits from the mesa.Agent super class
    def __init__(self, unique_id, model):
        super().__init__( model) # it inherits the model instance
        self.Tiles_cleaned = 0 # tile cleaned counter

        # we define the movement function for the agents
    def move(self):
        possible = self.model.grid.get_neighborhood(self.pos, moore = True , include_center = False) # this checks the agents' environment
        new_pos = self.random.choice(possible) # this picks the next position of movement at random
        # finish the movement
        self.model.grid.move_agent(self, new_pos)

        # we now have to define the cleaning task of the agent
    def clean(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other = self.random.choice(cellmates)
            if other != self:
                if isinstance(other, DirtyTile):
                    if other.Dirt > 0:
                        self.Tiles_cleaned += 1
                        other.Dirt -= 1
                        if other.Dirt <= 0:
                            self.model.grid.remove_agent(other)


    # we define the step method
    def step(self):
        self.move()
        self.clean()


class DirtyTile(mesa.Agent):
    def __init__(self, unique_id ,  model):
        super().__init__(model)
        self.Dirt = 1 # each tile has 1 unit of Dirt so that the tile is cleaned once and for all



class Room_Model(mesa.Model):
    def __init__(self, N, D,width,height):
        super().__init__()
        self.Num_of_robots = N
        self.Dirty = D
        self.grid = mesa.space.MultiGrid(width,height,torus = True)

        for i in range(self.Num_of_robots):
            a = Robot_Agent(i, self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.width)
            self.grid.place_agent(a,(x,y))

        for j in range(self.Dirty):
            b = DirtyTile(j,self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(b,(x,y))

    def step(self):
        self.agents.shuffle_do("step")





model = Room_Model(50,100,30,30)
for i in range(1000):
    print(f"step {i}")
    model.step()


# tiles cleaned vs number of agents
tiles = []
for agents in model.agents:
    if isinstance(agents, Robot_Agent):
        tiles.append(agents.Tiles_cleaned)

if tiles:
    plt.figure(figsize =(10,10))
    sns.histplot(tiles, bins = range(max(tiles)+2), kde = True , stat = "count", discrete = True, edgecolor = "black")
    plt.title("HISTOGRAM OF TILES CLEANED")
    plt.xlabel("TILES CLEANED")
    plt.ylabel("NUMBER OF ROBOTS")
    plt.grid(True, alpha = 0.3)
    plt.show()

# dirty tiles  that were left uncleaned
dirty = []
for agents in model.agents:
    if isinstance(agents, DirtyTile):
        dirty.append(agents.Dirt)

if dirty:
    plt.figure(figsize = (10,10))
    sns.histplot(dirty, bins = range(max(dirty)+2), kde = True , stat = "count", discrete = True , edgecolor = "black")
    plt.title("HISTOGRAM FOR DIRTY TILES")
    plt.xlabel("DIRTY TILES")
    plt.ylabel("NUMBER OF TILES")
    plt.grid(True, alpha = 0.3)
    plt.show()
else:
    print("All the tiles are cleaned successfully")










