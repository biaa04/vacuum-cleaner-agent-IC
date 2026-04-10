import random

class VaccumAgentSimple:

    def action(self, percept):
        if percept == "sujo":
            return "limpar", random.choice(["esquerda", "direita", "cima", "baixo"])
        else:
            return "mover", random.choice(["esquerda", "direita", "cima", "baixo"])