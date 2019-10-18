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

import matplotlib.pyplot as plt
import numpy as np
#from batchrun import batch_run
from mesa.batchrunner import BatchRunner


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
            if i < len(self.fibroblast_area):
                coord = self.fibroblast_area[i]
            else:
                coord = int(self.random.randrange(len(self.fibroblast_area)))
                coord = self.fibroblast_area[coord]
            x = coord[0]
            y = coord[1]
            a = Fibroblast(self.next_id(), (x, y), self)
            self.schedule.add(a)
            self.grid.place_agent(a, (x, y))

        self.running = True

        self.datacollector = DataCollector(model_reporters={"Blood_flow": Blood_flow,"Collagen": Collagen, "Macrophages": lambda self: self.schedule.get_breed_count(Macrophage), "Neutrophils": lambda self: self.schedule.get_breed_count(Neutrophil), "Fibroblasts": lambda self: self.schedule.get_breed_count(Fibroblast), "Necrotic_neutrophils": lambda self: self.schedule.get_neutrophiltype_count(Neutrophil,"Necrotic"),"Apoptised_neutrophils": lambda self: self.schedule.get_neutrophiltype_count(Neutrophil,"Apoptotic"),"Phagocytized_neutrophils":lambda self: self.schedule.get_neutrophiltype_count(Neutrophil,"Phagocytized"), "TGFb":lambda self: heatmap(self, "TGFB"), "IL6": lambda self: heatmap(self, "IL6"), "IL10": lambda self: heatmap(self, "IL10"), "TNFa": lambda self: heatmap(self, "TNFa"), "Mac_phen": MacrophagePhenotypes, "Cytokines":NetCytokines})

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




def Blood_flow(model):
    agent_oxy = [agent.oxy for agent in model.schedule.agents if type(agent) is Endothelial and agent.pos in model.wound_coord]
    oxy_total = sum(agent_oxy)

    return oxy_total/(len(model.wound_coord))

def Collagen(model):
    agent_coll = [agent.coll for agent in model.schedule.agents if type(agent) is Endothelial and agent.pos in model.wound_coord]
    coll_total = sum(agent_coll)
    return coll_total/len(model.wound_coord)

def MacrophagePhenotypes(model):
	mac_1 = 0
	mac_2 = 0
	for agent in model.schedule.agents:
		if type(agent) is Macrophage and agent.energy>0:
			if(agent.phenotype == 0): mac_1 += 1
			else: mac_2 += 1
	return [mac_1, mac_2]


def heatmap(model, entity):
    map = []
    for agent in model.schedule.agents:
        if type(agent) is Endothelial:
            if entity == "TGFB":
                map.append([agent.pos, agent.TGFb])
            elif entity == "IL6":
                map.append([agent.pos, agent.IL6])
            elif entity == "IL10":
                map.append([agent.pos, agent.IL10])
            elif entity == "TNFa":
                map.append([agent.pos, agent.TNFa])
    return np.array(map)

def NetCytokines(model):
	IL6, IL10, TNFa, TGFb = 0,0,0,0
	for agent in model.schedule.agents:
		if type(agent) is Endothelial and agent.pos in model.wound_coord:
			IL6 += agent.IL6
			IL10 += agent.IL10
			TNFa += agent.TNFa
			TGFb += agent.TGFb
	return [IL6, IL10, TNFa, TGFb]

