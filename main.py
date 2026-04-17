from environment import Environment as En
from tools import salvar_simulacao_txt
from vaccum_agent_simple import VaccumAgentSimple 
from vaccum_agent_model import VaccumAgentModel

def simular_simples():
    """Simula o agente aspirador simples em um ambiente pré-definido. O ambiente é 
    representado por uma matriz 5x5, onde cada célula pode conter os seguintes valores:
    - "sujo": indica que a célula está suja e precisa ser limpa.
    - "limpo": indica que a célula está limpa.
    - "obst": indica que a célula contém um obstáculo que o agente deve evitar.
    O agente começa na posição (0, 0) e tem uma pontuação inicial de zero. 
    O agente toma decisões com base na percepção atual do ambiente, limpando se estiver
    sujo, reconhecendo quando o ambiente está limpo e desviando de obstáculos. 
    A simulação continua até que o agente tenha tomado 100 passos ou até que não 
    haja mais células sujas no ambiente. Os resultados da simulação são salvos em um 
    arquivo de texto para análise posterior."""

    ambiente = [
        ["sujo", "limpo", "sujo", "sujo", "limpo"],
        ["limpo", "sujo", "obst", "sujo", "limpo"],
        ["sujo", "obst", "sujo", "limpo", "sujo"],
        ["limpo", "sujo", "limpo", "sujo", "obst"],
        ["sujo", "obst", "sujo", "limpo", "sujo"]
    ]
    agente = VaccumAgentSimple()
    env = En(agente, ambiente)
    initial_infos = {
        "Posição inicial": agente.position,
        "Estado inicial do grid": env.grid,
        "Pontuação inicial": agente.score
    }
    infos = []

    aux = True

    while aux:
        percepcao = agente.percept(env.grid)
        acao, direcao = agente.action(percepcao)
        env.action_in_env(acao, direcao)
        infos.append({
            "Passo": env.steps,
            "Percepção": percepcao,
            "Ação": acao,
            "Direção": direcao,
            "Posição": agente.position,
            "Pontuação": agente.score,
            "Estado do grid": env.grid,
        })

        if env.steps >= 100 or not any("sujo" in linha for linha in env.grid):
            aux = False
        
    
    salvar_simulacao_txt(initial_infos, infos, "resultado_simulacao_simples.txt")

def simular_model():

    """Simula o agente aspirador modelo em um ambiente pré-definido. O ambiente é
        representado por uma matriz 5x5, onde cada célula pode conter os seguintes valores:
        - "sujo": indica que a célula está suja e precisa ser limpa.
        - "limpo": indica que a célula está limpa.
        - "obst": indica que a célula contém um obstáculo que o agente deve evitar.
        O agente começa na posição (0, 0) e tem uma pontuação inicial de zero.
        O agente possui uma memória para evitar repetir ações em posições já visitadas. Ele também tem a 
        capacidade de verificar se todo o ambiente está limpo, o que o torna mais eficiente na limpeza do que 
        o agente simples. Ele também desvia de obstáculos escolhendo outra direção para seguir. A simulação 
        continua até que o agente tenha tomado 100 passos ou até que não haja mais células sujas no ambiente. 
        Os resultados da simulação são salvos em um arquivo de texto para análise posterior.
    """

    ambiente = [
        ["sujo", "limpo", "sujo", "sujo", "limpo"],
        ["limpo", "sujo", "obst", "sujo", "limpo"],
        ["sujo", "obst", "sujo", "limpo", "sujo"],
        ["limpo", "sujo", "limpo", "sujo", "obst"],
        ["sujo", "obst", "sujo", "limpo", "sujo"]
    ]
    agente = VaccumAgentModel()
    env = En(agente, ambiente)
    initial_infos = {
        "Posição inicial": agente.position,
        "Estado inicial do grid": env.grid,
        "Pontuação inicial": agente.score
    }
    infos = []

    aux = True

    while aux:
        percepcao = agente.percept(env.grid)
        print(f"Percepção: {percepcao}, Posição: {agente.position}, Pontuação: {agente.score}")
        acao, direcao = agente.action(percepcao)
        env.action_in_env(acao, direcao)
        print(f"Passo: {env.steps}, Percepção: {percepcao}, Ação: {acao}, Direção: {direcao}, Posição: {agente.position}, Pontuação: {agente.score}")
        print("Memory:", agente.memory)
        if acao != "mover":
            infos.append({
                "Passo": env.steps,
                "Percepção": percepcao,
                "Ação": acao,
                "Direção": direcao,
                "Posição": agente.position,
                "Pontuação": agente.score,
                "Estado do grid": env.grid,
            })  
        if agente.all_clean(env.grid):
            aux = False

    salvar_simulacao_txt(initial_infos, infos, "resultado_simulacao_modelo.txt")

def main():

    cont = True

    while cont:
        print("Agente Aspirador")
        print("1. Agente Simples")
        print("2. Agente Modelo")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            simular_simples()
        elif opcao == "2":
            simular_model()
        elif opcao == "3":
            cont = False
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()