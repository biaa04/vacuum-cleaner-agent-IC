
import random

class VaccumAgentModel:

    """O agente aspirado modelo é uma evolução do agente simples, que possui uma memória para evitar repetir ações
      em posições já visitadas. Ele também tem a capacidade de verificar se todo o ambiente está limpo, 
      o que o torna mais eficiente na limpeza do que o agente simples. Ele também desvia de obstáculos escolhendo 
      outra direção para seguir."""

    def __init__(self):
        """Inicializa o agente com pontuação zero, posição inicial (0, 0) 
        e uma memória vazia para rastrear as posições visitadas."""
        self.score = 0
        self.position = (0, 0)
        self.memory = set()
        

    def action(self, percept):

        """Determina a ação a ser tomada com base na percepção atual do ambiente.
        Se a posição atual já foi visitada, o agente decide mover-se para uma direção aleatória para explorar novas áreas. Caso contrário, o agente adiciona a posição atual à memória e decide a ação com base na percepção:
        - Se a percepção for "sujo", o agente decide limpar.
        - Se a percepção for "limpo", o agente reconhece que o ambiente está limpo e pode escolher mover-se para explorar outras áreas.
        - Se a percepção for "obst", o agente reconhece um obstáculo e decide mover-se para evitar colidir com ele.
        O agente retorna a ação escolhida e a direção para a qual se moverá ou realizará a ação."""

        if self.position in self.memory:
            return "mover", random.choice(["esquerda", "direita", "cima", "baixo"])

        self.memory.add(self.position)

        if percept == "sujo":
            return "limpar", random.choice(["esquerda", "direita", "cima", "baixo"])
        else:
            if percept == "limpo":
                return "Ambiente Limpo", random.choice(["esquerda", "direita", "cima", "baixo"])
            else:
                return "obst", random.choice(["esquerda", "direita", "cima", "baixo"])


    def all_clean(self, grid):
        """Verifica se todo o ambiente está limpo. O agente percorre cada célula do grid e verifica se há alguma célula suja. 
        Se encontrar uma célula suja, retorna False, indicando que o ambiente ainda não está completamente limpo. Se percorrer 
        todo o grid sem encontrar células sujas, retorna True, indicando que o ambiente está completamente limpo."""
        for row in grid:
            for cell in row:
                if cell == "sujo":
                    return False
        return True
    
    def percept(self, grid):
        """Obtém a percepção do ambiente com base na posição atual do agente. 
        O agente acessa a célula do grid correspondente à sua posição atual e retorna o valor dessa 
        célula, que pode ser "sujo", "limpo" ou "obst". Essa percepção é usada para determinar a ação 
        a ser tomada pelo agente."""
        i, j = self.position
        return grid[i][j]