
import random

class VaccumAgentModel:

    def __init__(self):
        self.memory = []
        

    def action(self, percept):

        if percept in self.memory:
            return "mover", random.choice(["esquerda", "direita", "cima", "baixo"])

        self.memory.append(percept)

        if percept == "sujo":
            return "limpar", random.choice(["esquerda", "direita", "cima", "baixo"])
        else:
            if percept == "limpo":
                return "Ambiente Limpo", random.choice(["esquerda", "direita", "cima", "baixo"])
            else:
                return "obst", random.choice(["esquerda", "direita", "cima", "baixo"])