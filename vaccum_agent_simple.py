import random

class VaccumAgentSimple:

    """O agente aspirador simples é um agente reativo que toma decisões com base na percepção atual do ambiente. 
    Ele não possui memória e não leva em consideração ações passadas ou o estado geral do ambiente. 
    O agente simplesmente reage à percepção atual, limpando se estiver sujo, reconhecendo quando o ambiente está 
    limpo e desviando de obstáculos. Ele pode se mover em quatro direções: esquerda, direita, cima e baixo."""

    def __init__(self):
        """Inicializa o agente com pontuação zero e posição inicial (0, 0)."""
        self.score = 0
        self.position = (0, 0)

    def action(self, percept):
        """Determina a ação a ser tomada com base na percepção atual do ambiente.
        O agente decide a ação com base na percepção:
        - Se a percepção for "sujo", o agente decide limpar.
        - Se a percepção for "limpo", o agente reconhece que o ambiente está limpo e pode 
        escolher mover-se para explorar outras áreas.
        - Se a percepção for "obst", o agente reconhece um obstáculo e decide mover-se para evitar 
        colidir com ele.
        O agente retorna a ação escolhida e a direção para a qual se moverá ou realizará
        """
        if percept == "sujo":
            return "limpar", random.choice(["esquerda", "direita", "cima", "baixo"])
        else:
            if percept == "limpo":
                return "Ambiente Limpo", random.choice(["esquerda", "direita", "cima", "baixo"])
            else:
                return "obst", random.choice(["esquerda", "direita", "cima", "baixo"])
            
    def percept(self, grid):
        """Obtém a percepção do ambiente com base na posição atual do agente. 
        O agente acessa a célula do grid correspondente à sua posição atual e retorna o valor"""
        i, j = self.position
        return grid[i][j]
            