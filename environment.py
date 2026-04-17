import random


class Environment():
    """A classe Environment representa o ambiente em que o agente aspirador opera. 
    Ela é responsável por manter o estado do ambiente,"""
    def __init__(self, agent, grid: list = None):
        self.agent = agent
        self.steps = 0 
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    def action_in_env(self, action, direction):
        i, j = self.agent.position

        if action != "mover":
            self.steps += 1

        if action == "limpar":
            if self.grid[i][j] == "sujo":
                self.grid[i][j] = "limpo"
                self.agent.score += 1

        if action == "Ambiente Limpo":
            self.agent.score -= 1

        if action == "obst":
            self.agent.damage += 1

        if direction == "esquerda":
            if j > 0:
                self.agent.position = (i, j - 1)
            else:
                # SE O AGENTE TENTAR SE MOVER PARA FORA DO GRID, ELE RECEBE UM DANO E PERMANECE NA MESMA POSIÇÃO
                self.agent.damage += 1
                self.agent.position

        if direction == "direita":
            if j < self.width - 1:
                self.agent.position = (i, j + 1)
            else:
                self.agent.damage += 1
                self.agent.position

        if direction == "cima":
            if i > 0:
                self.agent.position = (i - 1, j)
            else:
                self.agent.damage += 1
                self.agent.position

        if direction == "baixo":
            if i < self.height - 1:
                self.agent.position = (i + 1, j)
            else:
                self.agent.damage += 1
                self.agent.position

    def all_clean(self):
        """Verifica se todo o ambiente está limpo. Essa função está no ambiente pois os agentes não são inteligentes
        o bastante para terem noção do ambiente todo. Essa função é equivalente ao humano perceber que o ambiente está limpo
        e desligar o aspirador."""
        for row in self.grid:
            for cell in row:
                if cell == "sujo":
                    return False
        return True
