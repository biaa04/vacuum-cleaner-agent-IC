import random

class Environment():
    def __init__(self, grid: list = None):
        self.width = 5
        self. height = 5
        self.position = (0, 0)
        self.score = 0
        if grid is None:
            self.grid = [ [random.choice(["sujo", "limpo"]) for _ in range(width)] 
                         for _ in range(height) ]
        else:
            self.grid = grid

    def percept(self):
        i, j = self.position
        return self.grid[i][j]
    
    def action_in_env(self, action, direction):
        i, j = self.position

        if action == "limpar":
            if self.grid[i][j] == "sujo":
                self.grid[i][j] = "limpo"
                self.score += 1
        
        if action == "Ambiente Limpo":
            self.score -= 1

        if direction == "esquerda":
            self.position = (i, j - 1) if j > 0 else self.position
        
        if direction == "direita":
            self.position = (i, j + 1) if j < self.width - 1 else self.position

        if direction == "cima":
            self.position = (i - 1, j) if i > 0 else self.position  

        if direction == "baixo":
            self.position = (i + 1, j) if i < self.height - 1 else self.position


    