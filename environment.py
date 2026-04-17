import random


class Environment():
    def __init__(self, agent, grid: list = None):
        self.width = 5
        self.height = 5
        self.agent = agent
        self.steps = 0 
        if grid is None:
            self.grid = [[random.choice(["sujo", "limpo"]) for _ in range(self.width)]
                         for _ in range(self.height)]
        else:
            self.grid = grid

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

        if direction == "esquerda":
            self.agent.position = (i, j - 1) if j > 0 else self.agent.position

        if direction == "direita":
            self.agent.position = (i, j + 1) if j < self.width - 1 else self.agent.position

        if direction == "cima":
            self.agent.position = (i - 1, j) if i > 0 else self.agent.position

        if direction == "baixo":
            self.agent.position = (i + 1, j) if i < self.height - \
                1 else self.agent.position
