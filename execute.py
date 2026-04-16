import tkinter as tk
from tkinter import ttk
import random
from environment import Environment
from vaccum_agent_model import VaccumAgentModel
from vaccum_agent_simple import VaccumAgentSimple


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Agente Aspirador")

        self.cell_size = 80

        # ================= CONTROLES =================
        control_frame = tk.Frame(root)
        control_frame.pack()

        # Seleção de agente
        tk.Label(control_frame, text="Agente").grid(row=0, column=0)

        self.agent_type = tk.StringVar(value="Simples")
        self.agent_menu = ttk.Combobox(
            control_frame,
            textvariable=self.agent_type,
            values=["Simples", "Modelo"],
            state="readonly",
            width=10
        )
        self.agent_menu.grid(row=0, column=1)

        # Quantidade de sujeira
        tk.Label(control_frame, text="Sujeiras").grid(row=1, column=0)
        self.dirt_entry = tk.Entry(control_frame, width=5)
        self.dirt_entry.insert(0, "10")
        self.dirt_entry.grid(row=1, column=1)

        # Quantidade de obstáculos
        tk.Label(control_frame, text="Obstáculos").grid(row=2, column=0)
        self.obst_entry = tk.Entry(control_frame, width=5)
        self.obst_entry.insert(0, "5")
        self.obst_entry.grid(row=2, column=1)

        # Botão start
        self.start_btn = tk.Button(control_frame, text="START", command=self.start_simulation)
        self.start_btn.grid(row=3, column=0, columnspan=2, pady=5)

        # ================= CANVAS =================
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.running = False

    # ================= INICIALIZAÇÃO =================
    def start_simulation(self):
        width, height = 5, 5

        dirt = int(self.dirt_entry.get())
        obst = int(self.obst_entry.get())

        # cria grid limpo
        grid = [["limpo" for _ in range(width)] for _ in range(height)]

        # adiciona sujeira
        for _ in range(dirt):
            i, j = random.randint(0, 4), random.randint(0, 4)
            grid[i][j] = "sujo"

        # adiciona obstáculos
        for _ in range(obst):
            i, j = random.randint(0, 4), random.randint(0, 4)
            grid[i][j] = "obst"

        # cria ambiente
        self.env = Environment(grid)

        # escolhe agente
        if self.agent_type.get() == "Simples":
            self.agent = VaccumAgentSimple()
        else:
            self.agent = VaccumAgentModel()

        self.running = True
        self.update_simulation()

    # ================= DESENHO =================
    def draw_grid(self):
        self.canvas.delete("all")

        for i in range(self.env.height):
            for j in range(self.env.width):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                cell = self.env.grid[i][j]

                if cell == "sujo":
                    color = "brown"
                elif cell == "limpo":
                    color = "white"
                else:  # obstáculo
                    color = "black"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

        # desenha agente
        i, j = self.env.position
        x1 = j * self.cell_size + 10
        y1 = i * self.cell_size + 10
        x2 = x1 + self.cell_size - 20
        y2 = y1 + self.cell_size - 20

        self.canvas.create_oval(x1, y1, x2, y2, fill="blue")

    # ================= LOOP =================
    def update_simulation(self):
        if not self.running:
            return

        percept = self.env.percept()

        action, direction = self.agent.action(percept)

        # evita entrar em obstáculo
        i, j = self.env.position
        next_pos = {
            "esquerda": (i, j - 1),
            "direita": (i, j + 1),
            "cima": (i - 1, j),
            "baixo": (i + 1, j)
        }.get(direction, (i, j))

        ni, nj = next_pos
        if 0 <= ni < self.env.height and 0 <= nj < self.env.width:
            if self.env.grid[ni][nj] != "obst":
                self.env.action_in_env(action, direction)
        else:
            self.env.action_in_env(action, None)

        self.draw_grid()

        self.root.after(500, self.update_simulation)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()