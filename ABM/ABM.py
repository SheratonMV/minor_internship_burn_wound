'''
Wound healing ABM Prediction Model
================================
'''

from mesa.space import MultiGrid
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from agents import Neutrophil, Macrophage, Fibroblast, Endothelial
from coordinates import *
from schedule import RandomActivationByAgent
from mesa.batchrunner import BatchRunner
import matplotlib.pyplot as plt


class WoundModel(Model):
    """An ABM wound healing model simulating inflammation and contraction."""
    def __init__(self, Neutrophils, Macrophages, Fibroblasts, IL10,IL6,TNFa,TGFb,  width, height, wound_radius, coagulation):

        self.running = True
        self.neutrophils = Neutrophils
        self.macrophages = Macrophages
        self.fibroblasts = Fibroblasts
        self.IL10 = IL10
        self.IL6 = IL6
        self.TNFa = TNFa
        self.TGFb = TGFb
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivationByAgent(self)
        self.current_id = 0
        self.centre = (width//2, height//2)
        self.coagulation_size = wound_radius * coagulation
        self.resting_neutrophils = 0
        self.resting_macrophages = 0
        self.resting_fibroblasts = 0
        self.timer = 0


        #create wound and non-wound region
        self.all_coordinates = all_coordinates(self.grid.width, self.grid.height)
        self.wound_radius = wound_radius
        #self.wound_coord = square_wound_area(self.grid.width, self.grid.height, self.wound_radius) # square shaped wound
        self.wound_coord = circle_wound_area(self.grid.width, self.grid.height, self.wound_radius, self.all_coordinates) #ellipse shaped wound
        self.coagulation_coord = circle_wound_area(self.grid.width, self.grid.height, self.coagulation_size, self.all_coordinates)
        self.healthy = circle_wound_area(self.grid.width, self.grid.height, self.wound_radius+1, self.all_coordinates)

        self.non_wound_coord = []
        self.inflammation_coord = []
        self.fibroblast_area = []
        for coordinates in self.wound_coord:
            if coordinates not in self.coagulation_coord:
                self.inflammation_coord += [coordinates]

        for coordinates in self.healthy:
            if coordinates not in self.wound_coord:
                self.fibroblast_area += [coordinates]

        for coordinates in self.all_coordinates:
            if coordinates not in self.wound_coord:
                self.non_wound_coord += [coordinates]

        # Create non-wound Endothelial cells
        for i in range(len(self.non_wound_coord)):
            # Add the agent in the non wound-region
            coord = self.non_wound_coord[i]
            a = Endothelial(self.next_id(),(coord[0],coord[1]),100,100,0,0,0,0,self)
            self.schedule.add(a)
            self.grid.place_agent(a, (coord[0], coord[1]))

        # Create wound Endothelial-cells
        for i in range(len(self.wound_coord)):
            # Add the agent in the wound-region
            coord = self.wound_coord[i]
            if(coord in self.coagulation_coord):
                a = Endothelial(self.next_id(),(coord[0],coord[1]),0,0,0,0,0,0, self)
            else:
                a = Endothelial(self.next_id(),(coord[0],coord[1]),25,0,self.IL10, self.IL6,self.TNFa,self.TGFb,self)
            self.schedule.add(a)
            self.grid.place_agent(a, (coord[0], coord[1]))

        # Create Neutrophils
        for i in range(self.neutrophils):

            # Add the agent in a non-wound region
            coord = int(self.random.randrange(len(self.inflammation_coord)))
            coord = self.inflammation_coord[coord]
            x = coord[0]
            y = coord[1]
            a = Neutrophil(self.next_id(), (x,y),self.centre, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (x, y))

        # Create Macrophages
        for i in range(self.macrophages):

            # Add the agent in a non-wound region
            coord = int(self.random.randrange(len(self.inflammation_coord)))
            coord = self.inflammation_coord[coord]
            x = coord[0]
            y = coord[1]
            a = Macrophage(self.next_id(),(x,y), self)
            self.schedule.add(a)
            self.grid.place_agent(a, (x, y))

        # Create Fibroblasts
        for i in range(self.fibroblasts):
            # Add the agent in a non-wound region
            coord = int(self.random.randrange(len(self.fibroblast_area)))
            coord = self.fibroblast_area[coord]
            x = coord[0]
            y = coord[1]
            a = Fibroblast(self.next_id(), (x, y), self)
            self.schedule.add(a)
            self.grid.place_agent(a, (x, y))

        self.running = True

        self.datacollector = DataCollector(model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen, "Macrophages": Macrophage_count, "Neutrophils": Neutrophil_count, "Fibroblasts": Fibroblast_count})




    def blood_flow(self):
        agent_oxy = [agent.oxy for agent in self.schedule.agents if type(agent) is Endothelial]
        oxy_total = sum(agent_oxy)
        return oxy_total / 62550 * 100



    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        self.timer += 1
        if self.timer % 2:
            self.resting_neutrophils += 2

        if self.timer % 2:
            self.resting_macrophages += 2

        if self.timer % 6:
            self.resting_fibroblasts += 2

        print(self.resting_neutrophils)
        #cell_concentrations = self.datacollector.get_model_vars_dataframe()
        #print(cell_concentrations)






def Blood_flow(model):
    agent_oxy = [agent.oxy for agent in model.schedule.agents if type(agent) is Endothelial]
    oxy_total = sum(agent_oxy)
    return oxy_total/62550 *100

def Collagen(model):
    agent_coll = [agent.coll for agent in model.schedule.agents if type(agent) is Endothelial]
    coll_total = sum(agent_coll)
    return coll_total/62550 * 100

def Fibroblast_count(model):
     fibroblast_count = 0
     for agent in model.schedule.agents:
         if type(agent) is Fibroblast and agent.energy > 0:
            fibroblast_count += 1
     return fibroblast_count

def Neutrophil_count(model):
     neutrophil_count = 0
     for agent in model.schedule.agents:
         if type(agent) is Neutrophil and agent.energy > 0:
            neutrophil_count += 1
     return neutrophil_count

def Macrophage_count(model):
     macrophage_count = 0
     for agent in model.schedule.agents:
         if type(agent) is Macrophage and agent.energy > 0:
            macrophage_count += 1
     return macrophage_count


def batch_run(WoundModel):

    fixed_params = {
    "Neutrophils": 80,
     "Macrophages": 80,
     "Fibroblasts": 80,
     "IL10": 0,
     "IL6": 0,
     "TNFa": 0,
     "TGFb": 0,
     "width": 25,
     "height": 25,
     "wound_radius": 10,
     "coagulation": 0.7
    }

    batch_run = BatchRunner(
    WoundModel,variable_parameters=None,
    fixed_parameters = fixed_params,
    max_steps=100,
    model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen, "Macrophages": Macrophage_count, "Neutrophils": Neutrophil_count, "Fibroblasts": Fibroblast_count}
    )

    batch_run.run_all()
    run_data = batch_run.get_model_vars_dataframe()
    print(run_data)

#batch_run(WoundModel)

def loop_fig(fignum):
    return fignum + 1

def run_model(step_count=100):
    model = WoundModel(40,50,80,0.5,0,0,0,25,25,10,0.7)
    for i in range(step_count):
        model.step()
    cell_concentrations = model.datacollector.get_model_vars_dataframe()


    modelAP = WoundModel(80, 50, 80, 1, 0, 0, 0, 25, 25, 10, 0.7)
    for i in range(step_count):
        modelAP.step()
    cell_concentrationsAP = modelAP.datacollector.get_model_vars_dataframe()


    lw = 5
    ls = 20
    fs = 25
    lfs = 25
    ts = 30

    n = loop_fig(1)
    plt.figure(n)
    plt.plot(cell_concentrations["Macrophages"], linewidth=lw, ls='-', color = "#377eb8" )
    plt.plot(cell_concentrationsAP["Macrophages"], linewidth=lw, ls='-', color = "#4daf4a")
    plt.ylabel("Macrophages (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.title("Macrophages", fontsize=ts)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting macrophages')
    plt.savefig('results/' + 'Macrophages.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Neutrophils"], linewidth=lw, ls='-', color = "#377eb8" )
    plt.plot(cell_concentrationsAP["Neutrophils"], linewidth=lw, ls='-', color = "#4daf4a")
    plt.ylabel("Neutrophils (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Neutrophils", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting neutrophils')
    plt.savefig('results/' + 'Neutrophils.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Fibroblasts"], linewidth=lw, ls='-', color = "#377eb8")
    plt.plot(cell_concentrationsAP["Fibroblasts"], linewidth=lw, ls='-', color = "#4daf4a" )
    plt.ylabel("Fibroblasts (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Fibroblasts", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting fibroblasts')
    plt.savefig('results/' + 'Fibroblasts.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)

    plt.plot(cell_concentrations["Blood_flow"], linewidth=lw, ls='-', color = "#377eb8" )
    plt.plot(cell_concentrationsAP["Blood_flow"], linewidth=lw, ls='-', color="#4daf4a")
    plt.ylabel("Oxygen (%)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Oxygen in wound", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting Oxygen')
    plt.savefig('results/' + 'oxygen.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)

    plt.plot(cell_concentrations["Collagen"], linewidth=lw, ls='-', color = "#377eb8" )
    plt.plot(cell_concentrationsAP["Collagen"], linewidth=lw, ls='-', color="#4daf4a")
    plt.ylabel("Collagen (%)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Collagen % over whole wound", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting collagen')
    plt.savefig('results/' + 'Collagen.png', format='png', dpi=500, bbox_inches='tight')

#run_model()