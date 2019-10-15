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
import numpy as np


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
        self.resting_neutrophils = 20
        self.resting_macrophages = 20
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

        self.datacollector = DataCollector(model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen, "Macrophages": Macrophage_count, "Neutrophils": Neutrophil_count, "Fibroblasts": Fibroblast_count, "TGFb": TGFb_heat})




    def blood_flow(self):
        agent_oxy = [agent.oxy for agent in self.schedule.agents if type(agent) is Endothelial]
        oxy_total = sum(agent_oxy)
        return oxy_total / len(self.all_coordinates)

    def Collagen(self):
        agent_coll = [agent.coll for agent in self.schedule.agents if type(agent) is Endothelial]
        coll_total = sum(agent_coll)
        return coll_total / len(self.all_coordinates)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        self.timer += 1

        if self.timer % 2 == 0:
            self.resting_neutrophils += 1

        if self.timer % 4 == 0:
            self.resting_macrophages += 1

        if self.timer % 8 == 0:
            self.resting_fibroblasts += 1

                #cell_concentrations = self.datacollector.get_model_vars_dataframe()
        #print(cell_concentrations)






def Blood_flow(model):
    agent_oxy = [agent.oxy for agent in model.schedule.agents if type(agent) is Endothelial and agent.pos in model.wound_coord]
    oxy_total = sum(agent_oxy)

    return oxy_total/(len(model.wound_coord))

def Collagen(model):
    agent_coll = [agent.coll for agent in model.schedule.agents if type(agent) is Endothelial and agent.pos in model.wound_coord]
    coll_total = sum(agent_coll)
    return coll_total/len(model.wound_coord)

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


def Neutrophil_necrotic_count(model):
    neutrophil_count = 0
    for agent in model.schedule.agents:
        if type(agent) is Neutrophil and agent.energy <= 0:
            if not agent.apoptised:
                neutrophil_count += 1
    return neutrophil_count

def Macrophage_count(model):
     macrophage_count = 0
     for agent in model.schedule.agents:
         if type(agent) is Macrophage and agent.energy > 0:
            macrophage_count += 1
     return macrophage_count

def TGFb_heat(model):
    T_map = []
    for agent in model.schedule.agents:
        if type(agent) is Endothelial:
            T_map.append([agent.pos, agent.TGFb])

    return np.array(T_map)



def batch_run(WoundModel):

    fixed_params = {
    "Neutrophils": 80,
     "Macrophages": 50,
     "Fibroblasts": 50,
     "IL10": 0.5,
     "IL6": 0.5,
     "TNFa": 0.5,
     "TGFb": 0.5,
     "width": 25,
     "height": 25,
     "wound_radius": 10,
     "coagulation": 0.7
    }

    batch_run = BatchRunner(
    WoundModel,variable_parameters=None,
    fixed_parameters = fixed_params,
    max_steps=120,
    model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen, "Macrophages": Macrophage_count, "Neutrophils": Neutrophil_count, "Fibroblasts": Fibroblast_count}
    )

    batch_run.run_all()
    run_dataAP = batch_run.get_model_vars_dataframe()

    fixed_params = {
        "Neutrophils": 80,
        "Macrophages": 80,
        "Fibroblasts": 80,
        "IL10": 0.5,
        "IL6": 0.5,
        "TNFa": 0.5,
        "TGFb": 0.5,
        "width": 25,
        "height": 25,
        "wound_radius": 10,
        "coagulation": 0.5
    }

    batch_run = BatchRunner(
        WoundModel, variable_parameters=None,
        fixed_parameters=fixed_params, iterations= 5,
        max_steps=120,
        model_reporters={"Blood_flow": Blood_flow, "Collagen": Collagen, "Macrophages": Macrophage_count,
                         "Neutrophils": Neutrophil_count, "Fibroblasts": Fibroblast_count}
    )

    batch_run.run_all()
    run_data = batch_run.get_model_vars_dataframe()

    print(run_data)

#batch_run(WoundModel)

def loop_fig(fignum):
    return fignum + 1

def run_model(step_count=120):
    model = WoundModel(50,50,50,0.5,0.5,0.5,0.5,25,25,10,0.5)
    for i in range(step_count):
        model.step()
    cell_concentrations = model.datacollector.get_model_vars_dataframe()

    modelAP = WoundModel(80, 50, 50, 4, 0.0, 0.5, 0.5, 25, 25, 10, 0.5)
    #modelAP = WoundModel(80, 50, 80, 1, 0, 0, 0, 25, 25, 10, 0.7)
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
    plt.ylim(0,100)
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
    plt.ylim(0, 100)
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
    plt.ylim(0, 100)
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
    plt.ylim(0, 100)
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
    plt.ylim(0, 100)
    plt.legend({ 'bIAP', 'Placebo'}, loc='best', fontsize=lfs)
    plt.title("Collagen % over whole wound", fontsize=ts)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting collagen')
    plt.savefig('results/' + 'Collagen.png', format='png', dpi=500, bbox_inches='tight')

#run_model()

def run_calibration(step_count=120):
    model = WoundModel(50,50,50,0.5,0.5,0.5,0.5,25,25,10,0.5)
    for i in range(step_count):
        model.step()
    cell_concentrations = model.datacollector.get_model_vars_dataframe()


    lw = 5
    ls = 10
    fs = 15
    lfs = 15
    ts = 15

    n = loop_fig(1)
    plt.figure(n)
    plt.plot(cell_concentrations["Macrophages"], linewidth=lw, ls='-')
    plt.plot(cell_concentrations["Neutrophils"], linewidth=lw, ls='-')
    plt.plot(cell_concentrations["Fibroblasts"], linewidth=lw, ls='-')
    plt.xlim(0,120)
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)

    plt.legend({ 'Fibroblasts', 'Macrophages', 'Neutrophils', }, loc='best', fontsize=lfs)
    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting macrophages')
    plt.savefig('results/' + 'all.png', format='png', dpi=500, bbox_inches='tight')

    n = loop_fig(n)
    plt.figure(n)
    plt.plot(cell_concentrations["Blood_flow"], linewidth=lw, ls='-', color = 'red')
    plt.plot(cell_concentrations["Collagen"], linewidth=lw, ls='-', color = 'black')
    plt.legend({'Oxygen', 'Collagen' }, loc='best', fontsize=lfs)
    plt.xlim(0, 120)
    plt.ylabel("Concentration (Arbitrary units)", fontsize=fs)
    plt.xlabel("Time (h)", fontsize=fs)

    plt.tick_params(labelsize=ls)
    plt.tight_layout()
    print('... Plotting macrophages')
    plt.savefig('results/' + 'blood.png', format='png', dpi=500, bbox_inches='tight')
    #plt.plot(cell_concentrations["Collagen"], linewidth=lw, ls='-')


#run_calibration()

def heat_map(step_count=120):
    model = WoundModel(50,50,50,0.5,0.5,0.5,0.5,25,25,10,0.5)
    for i in range(step_count):
        model.step()
    cell_concentrations = model.datacollector.get_model_vars_dataframe()


    lw = 5
    ls = 10
    fs = 15
    lfs = 15
    ts = 15

    #n = loop_fig(1)
    #plt.figure(n)
    #plt.plot(cell_concentrations["TGFb"], linewidth=lw, ls='-')
    #plt.savefig('results/' + 'TGFb.png', format='png', dpi=500, bbox_inches='tight')
    TG_map = cell_concentrations["TGFb"][119]
    Tmap = np.zeros((25,25))
    for x in TG_map:
        a, b = x[0][0],x[0][1]
        Tmap[a,b] = x[1]
    #plt.show()
    print(Tmap)
    plt.imshow(Tmap, cmap="hot")
    plt.savefig('results/' + 'tgfb.png', format='png', dpi=500, bbox_inches='tight')


    
    
heat_map()