
import random

class VaccumAgentModel:

    """O agente aspirado modelo é uma evolução do agente simples, que possui uma memória para evitar repetir ações
      em posições já visitadas."""

    def __init__(self):
        """Inicializa o agente com pontuação zero, danos zero,posição inicial (0, 0) 
        e uma memória vazia para rastrear as posições visitadas."""
        self.score = 0
        self.position = (0, 0)
        self.memory = None
        self.damage = 0
        

    def action(self, percept):

        """Determina a ação a ser tomada com base na percepção atual do ambiente.
        O agente decide a ação com base na percepção:
        - Se a percepção for "sujo", o agente decide limpar.
        - Se a percepção for "limpo", o agente reconhece que o ambiente está limpo e move-se em outra direção, mas ele perde ponto por limpar algo limpo.
        - Se a percepção for "obst", o agente reconhece um obstáculo e decide mover-se Na direção contrária.
        O agente retorna a ação escolhida e a direção para a qual se moverá ou realizará a ação."""

        direction_list = ["esquerda", "direita", "cima", "baixo"]

        opposite = {
            "esquerda": "direita",
            "direita": "esquerda",
            "cima": "baixo",
            "baixo": "cima"
        }

        available_directions = [
            d for d in direction_list
            if d != opposite.get(self.memory)
        ]

        direction = random.choice(available_directions)
        self.memory = direction

        if percept == "sujo":
            return "limpar", direction
        else:
            if percept == "limpo":
                return "Ambiente Limpo", direction
            else:
                return "obst", direction
            
    def direction(direction_list):
        """Escolhe uma direção aleatória da lista de direções disponíveis. Essa função é usada 
        para determinar a direção para a qual o agente se moverá ou realizará uma ação, 
        especialmente quando o agente precisa evitar obstáculos ou explorar novas áreas do ambiente."""
        return random.choice(direction_list)
    
    def percept(self, grid):
        """Obtém a percepção do ambiente com base na posição atual do agente. 
        O agente acessa a célula do grid correspondente à sua posição atual e retorna o valor dessa 
        célula, que pode ser "sujo", "limpo" ou "obst". Essa percepção é usada para determinar a ação 
        a ser tomada pelo agente."""
        i, j = self.position
        return grid[i][j]