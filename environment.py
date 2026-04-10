import random

class Environment():
    def __init__(self, width, height):
        self.width = width
        self. height = height
        self.grid = [ [random.choice(["sujo", "limpo"]) for _ in range(width)] 
                     for _ in range(height) ]

        self.position = (0, 0)
        self.score = 0

    def percept(self):
        i, j = self.position
        return self.grid[i][j]
    
    def action_in_env(self, action, direction):
        i, j = self.position

        if action == "limpar":
            if self.grid[i][j] == "sujo":
                self.grid[i][j] = "limpo"
                self.score += 1
        
        elif action == "mover":
            self.score -= 1

        elif direction == "esquerda":
            self.position = (i, j - 1) if j > 0 else self.position
        
        elif direction == "direita":
            self.position = (i, j + 1) if j < self.width - 1 else self.position

        elif direction == "cima":
            self.position = (i - 1, j) if i > 0 else self.position  

        elif direction == "baixo":
            self.position = (i + 1, j) if i < self.height - 1 else self.position


    