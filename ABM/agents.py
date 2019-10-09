import random
from mesa import Agent
import numpy as np
import math as m


class Endothelial(Agent):
    """" An Endotheial non-mobile agent imbedded in the grid-space of the model.
    variables:
    oxy -> oxygen level of the epithelial cell ranging from 0 to 25 (indicates the 'health' status)
    Oxy simulates the effect of downstream ischemia
    other celltypes can spawn on this part of the grid whenever oxy = 25
    """

    def __init__(self, unique_id, pos, oxy,coll, IL10, IL6,TNFa, TGFb, model):
        super().__init__(unique_id, model)
        self.oxy = oxy
        self.pos = pos
        self.IL6 = IL6
        self.IL10 = IL10
        self.TGFb = TGFb
        self.TNFa = TNFa
        self.coll = coll
        self.neutrophil_time = 0
        self.macrophage_time = 0
        self.fibroblast_time = 0



    def attract_neutrophil(self):
        a = Neutrophil(self.model.next_id(), self.pos, self.model.centre, self.model)
        self.model.schedule.add(a)
        self.model.grid.place_agent(a, self.pos)
        self.model.resting_neutrophils -= 1


    def attract_macrophage(self):
        a = Macrophage(self.model.next_id(), self.pos, self.model)
        self.model.schedule.add(a)
        self.model.grid.place_agent(a, self.pos)
        self.model.resting_macrophages -= 1

    def attract_fibroblast(self):
        a = Fibroblast(self.model.next_id(), self.pos, self.model)
        self.model.schedule.add(a)
        self.model.grid.place_agent(a, self.pos)
        self.model.resting_fibroblasts -= 1

    def decay_cytokines(self):
        # decay of cytokines
        if self.IL6 <= 0:
            self.IL6 = 0
        else:
            self.IL6 -= 0.02

        if self.IL10 <= 0:
            self.IL10 = 0
        else:
            self.IL10 -= 0.02

        if self.TNFa <= 0:
            self.TNFa = 0
        else:
            self.TNFa -= 0.02

        if self.TGFb <= 0:
            self.TGFb = 0
        else:
            self.TGFb -= 0.02


    def step(self):

        self.macrophage_time += 1
        self.fibroblast_time += 1

        if self.TNFa > 2 and self.oxy >= 25 and self.IL10 < 1.5 and self.macrophage_time % 2 == 0 and self.model.resting_macrophages > 0 and self.coll <100:
            self.attract_macrophage()
            self.macrophage_time = 0


        if self.TNFa > 1 and self.oxy >= 25 and self.IL6 > 1 and self.model.resting_neutrophils > 0 and self.oxy<100:
            self.attract_neutrophil()
            self.neutrophil_time = 0


        if self.TGFb > 5 and self.coll < 100 and self.fibroblast_time % 8 == 0  and self.model.resting_fibroblasts > 0 :
            self.attract_fibroblast()
            self.fibroblast_time = 0

        self.decay_cytokines()





class Neutrophil(Agent):
    """ An agent with fixed initial energy."""

    def __init__(self, unique_id, pos, centre, model):
        super().__init__(unique_id, model)
        self.energy = 1
        self.pos = pos
        self.centre = centre
        self.apoptotic_hours = 0
        self.apoptised = False

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=False)
        new_position = []

        # only migration over the non-wounded areas and to cell with highest TNFa.
        '''TNFa = []
        for agent in neighbors:
            if type(agent) is Endothelial:
                TNFa.append(agent.TNFa)

        TNFa.sort(reverse=True)
        new_position = []

        print(max(TNFa))
        if max(TNFa) == 0:
            for agent in neighbors:
                if type(agent) is Endothelial:
                    if agent.oxy == 100:
                        possible_steps.remove(agent.pos)
                    elif agent.coll == 100:
                        possible_steps.remove(agent.pos)
            new_position = possible_steps
            print('zero')

        else:
            print('nonzero')
            for a in TNFa:
                print(new_position)
                if new_position != []:
                    break

                for agent in neighbors:
                    if type(agent) is Endothelial:
                        if agent.TNFa == a:


                            if agent.oxy == 100:
                                pass
                            elif agent.coll == 100:
                                pass
                            else:
                                new_position.append(agent.pos)
                                break
                        else:
                            pass'''


        for agent in neighbors:
            if type(agent) is Endothelial:
                if agent.oxy >= 100:
                    possible_steps.remove(agent.pos)
                elif agent.coll >= 100:
                    possible_steps.remove(agent.pos)
                elif agent.oxy <= 20:
                    possible_steps.remove(agent.pos)
        new_position = possible_steps

        if new_position != []:
            new_position = self.random.choice(new_position)
            self.model.grid.move_agent(self, new_position)



    def update_cytokines(self):
        """" Updates Cytokine levels of all neighbours """
        neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=True)
        for agent in neighbors:
            if type(agent) is Endothelial and agent.pos == self.pos:
                #agent.TNFa += 0.01 - agent.IL10*0.01 - agent.TGFb* 0.01 + agent.IL6*0.01
                agent.TNFa += 0.002
            elif type(agent) is Endothelial:
                agent.TNFa += 0.001


    def heal(self):
        """" heals EC its on and the neighbors a bit"""

        #cellmates = self.model.grid.get_cell_list_contents([self.pos])

        neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=True)
        for agent in neighbors:
            if type(agent) is Endothelial and agent.pos == self.pos:
                if self.energy > 0:
                    if agent.oxy >= 100:
                        pass
                    else:
                        agent.oxy += 1
            elif type(agent) is Endothelial:
                if self.energy > 0:
                    if agent.oxy >= 100:
                        pass
                    else:
                        agent.oxy += 1

            if type(agent) is Macrophage:
                if self.energy == 0:
                    print('remove neutrophil')

    def necrosis(self):
        self.apoptotic_hours += 1
        if self.apoptotic_hours == 5 and self.apoptised == False:
            neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=True)
            for agent in neighbors:
                if type(agent) is Endothelial and agent.pos == self.pos:
                    # agent.TNFa += 0.01 - agent.IL10*0.01 - agent.TGFb* 0.01 + agent.IL6*0.01
                    agent.TNFa += 0.004
                    agent.oxy -= 10
                elif type(agent) is Endothelial:
                    agent.TNFa += 0.002
                    agent.oxy -= 5


    def step(self):
        """Step:
        if energy < 0: neutrophil is considered apoptised"""


        if self.energy <= 0:
            self.necrosis()
        else:
            self.move()
            self.update_cytokines()
            self.heal()

            #lifespan is ~ 2 days energy represents life span
            cellmates = self.model.grid.get_cell_list_contents([self.pos])
            for agent in cellmates:
                if type(agent) is Endothelial:
                    energy_loss_IL10 = agent.IL10 *0.1


            self.energy = self.energy - 0.03 - energy_loss_IL10






class Macrophage(Agent):
    """ A Macrophage agent"""

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.energy = 1
        self.pos = pos

        # Phenotype M1 is 0/false, whilst M2 is 1/true
        self.phenotype = 0
        self.centre = model.centre

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=False)

        # only migration over the non-wounded areas.
        for agent in neighbors:
            if type(agent) is Endothelial:
                if agent.oxy < 20:
                    possible_steps.remove(agent.pos)
                elif agent.coll >= 100:
                    possible_steps.remove(agent.pos)


        if possible_steps == []:
            pass
        else:
            new_position = self.random.choice(possible_steps)
            self.model.grid.move_agent(self, new_position)

    def secrete(self):
        neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=True)
        counter = 0
        modulation = 0

        if (self.phenotype == 0):
            for agent in neighbors:
                if type(agent) is Endothelial:
                    agent.IL6 = agent.IL6 + 0.03
                    agent.TNFa = agent.TNFa + 0.03
                    if agent.oxy >= 100:
                        pass
                    else:
                        agent.oxy += 1
                    counter = counter + 2
                    modulation = modulation + agent.TNFa + agent.IL6
            if modulation / counter > 2:
                self.phenotype = 1

        else:
            for agent in neighbors:
                if type(agent) is Endothelial:
                    agent.TGFb = agent.TGFb + 0.1
                    agent.IL10 = agent.IL10 + 0.07
                    agent.TNFa = agent.TNFa + 0.01
            self.energy = self.energy - 0.05

    def apoptise_neutrophil(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        for agent in cellmates:
            if type(agent) == Neutrophil and agent.energy <= 0 and agent.apoptised == False:
                agent.apoptised = True




    def step(self):
        if self.energy <= 0:
            pass
        else:
            self.move()
            self.secrete()
            self.apoptise_neutrophil()

            # lifespan is ~ 4 days energy represents life span
            self.energy -= 0.004


class Fibroblast(Agent):
    """ A fibroblast agent has an energy variable representing the lifespan. if energy == 0 than fibroblast is apoptised.
    Each activated has a specific amount of collagen it can secrete. The amount of secretion after each step depends on the TGFb concentration """

    def __init__(self, unique_id, pos, model):
        super().__init__(unique_id, model)
        self.energy = 1
        self.pos = pos
        self.collagen = 1000
        self.TGFb_production = 0.01
        self.collagen_secretion = 1

    def move(self):
        """ Move over wounded region where oxygen >=25"""
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=False)

        for agent in neighbors:
            if type(agent) is Endothelial:
                if agent.coll >= 100:
                    possible_steps.remove(agent.pos)
                elif agent.oxy < 25:
                    possible_steps.remove(agent.pos)

        if possible_steps != []:
            new_position = self.random.choice(possible_steps)
            self.model.grid.move_agent(self, new_position)

    def secrete_collagen(self):
        """ secrete collagen on cell its sitting on based on TGFb concentration"""
        neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=True)
        TGFb_neigbors = []
        IL6_neigbors = []
        for agent in neighbors:
            if type(agent) is Endothelial:
                TGFb_neigbors += [agent.TGFb]
                IL6_neigbors += [agent.IL6]

        #actually 1+ deactivating cytokines but not included in this model
        Collagen_stimulation_factor = m.log((1 + sum(TGFb_neigbors)/9 + sum(IL6_neigbors)/9)/1)


        for agent in neighbors:
            if type(agent) is Endothelial and agent.pos == self.pos:
                if agent.coll < 100 and self.collagen >= self.collagen_secretion:
                    agent.coll += self.collagen_secretion * Collagen_stimulation_factor
                    self.collagen -= self.collagen_secretion * Collagen_stimulation_factor
            elif type(agent) is Endothelial:
                if agent.coll < 100 and self.collagen >= self.collagen_secretion:
                    agent.coll += self.collagen_secretion * Collagen_stimulation_factor
                    self.collagen -= self.collagen_secretion * Collagen_stimulation_factor


    def secrete_TGFb(self):
        neighbors = self.model.grid.get_neighbors(self.pos, 1, include_center=True)
        for agent in neighbors:
            if type(agent) is Endothelial and agent.pos == self.pos:
                agent.TGFb += self.TGFb_production
            elif type(agent) is Endothelial:
                agent.TGFb += self.TGFb_production/10


    def step(self):
        """ Step"""
        # only migration over the non-wounded areas.
        if self.model.blood_flow() > 90:

            cellmates = self.model.grid.get_cell_list_contents([self.pos])
            for agent in cellmates:
                if type(agent) is Endothelial:
                    if agent.coll >= 100 and agent.oxy >= 25:
                        self.move()
                        self.energy -= 0.002

                    elif agent.coll <100 and agent.oxy >= 25:
                        self.secrete_collagen()
                        self.secrete_TGFb()
                        self.energy -= 0.005

        #if self.model.col








