from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from ABM import WoundModel
from agents import *


Neutrophil_slider = UserSettableParameter('slider', "Number of Neutrophils", 50, 1, 100, 1)
Macrophage_slider = UserSettableParameter('slider', "Number of Macrophages", 50, 1, 100, 1)
Fibroblast_slider = UserSettableParameter('slider', "Number of Fibroblasts", 100, 1, 200, 1)
wound_size_slider = UserSettableParameter('slider', 'Wound Radius',10,1,10,1)
coagulation_slider = UserSettableParameter('slider', 'Proportion of Coagulation', 0.7, 0, 1, 0.1)
IL10_slider = UserSettableParameter('slider', 'Initial IL-10', 0, 0, 1, 0.1)
IL6_slider = UserSettableParameter('slider', 'Initial IL6', 0, 0, 1, 0.1)
TNFa_slider = UserSettableParameter('slider', 'Initial TNFa', 0, 0, 1, 0.1)
TGFb_slider = UserSettableParameter('slider', 'Initial TGFb', 0, 0, 1, 0.1)
grid_width = 25
grid_height = 25

def agent_portrayal(agent):
    portrayal = {"Shape": "rect",
                 "Filled": "true",
                 "w": 1, "h": 1}

    if type(agent) is Endothelial:
        if agent.oxy >= 25 and agent.coll >= 100:

            portrayal["Color"] = "tan"
            portrayal["Layer"] = 0
        elif agent.oxy >= 25 and agent.coll >= 100:
            portrayal["Color"] = "#FFA54F"
            portrayal["Layer"] = 0
        elif agent.oxy >= 25 and agent.coll < 100:
            portrayal["Color"] = "red"
            portrayal["Layer"] = 0
        elif agent.oxy < 25:
            portrayal["Color"] = "black"
            portrayal["Layer"] = 0



    elif type(agent) is Neutrophil:
        if agent.energy > 0:
            portrayal["Color"] = "green"
            portrayal["Layer"] = 1
            portrayal['Shape'] = "circle"
            portrayal['r'] = 0.5
        else:
            portrayal = {}

    elif type(agent) is Macrophage:
        if agent.energy > 0:
            if agent.phenotype == 0:
                portrayal["Color"] = "blue"
                portrayal["Layer"] = 1
                portrayal['Shape'] = "circle"
                portrayal['r'] = 0.5
            else:
                portrayal["Color"] = "cyan"
                portrayal["Layer"] = 1
                portrayal['Shape'] = "circle"
                portrayal['r'] = 0.5
        else:
            portrayal = {}

    elif type(agent) is Fibroblast:
        if agent.energy > 0:
            portrayal["Color"] = "purple"
            portrayal["Layer"] = 2
            portrayal['Shape'] = "circle"
            portrayal['r'] = 0.5
        else:
            portrayal = {}



    return portrayal

grid = CanvasGrid(agent_portrayal, grid_width,grid_height, 500, 500)


server = ModularServer(WoundModel,
                       [grid],
                       "Burn Wound Healing Model",
                       {"Neutrophils": Neutrophil_slider, "Macrophages": Macrophage_slider, "Fibroblasts": Fibroblast_slider,"IL10": IL10_slider, "IL6": IL6_slider,"TNFa": TNFa_slider, "TGFb": TGFb_slider, "width": grid_width, "height": grid_height, "wound_radius": wound_size_slider, "coagulation": coagulation_slider})


