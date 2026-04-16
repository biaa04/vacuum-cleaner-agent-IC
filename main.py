from environment import Environment as En
from tools import format_simulation_results
from vaccum_agent_simple import VaccumAgentSimple 

def simular():
    ambiente = [
        ["sujo", "limpo", "sujo", "sujo", "limpo"],
        ["limpo", "sujo", "obst", "sujo", "limpo"],
        ["sujo", "obst", "sujo", "limpo", "sujo"],
        ["limpo", "sujo", "limpo", "sujo", "obst"],
        ["sujo", "obst", "sujo", "limpo", "sujo"]
    ]
    env = En(ambiente)
    agente = VaccumAgentSimple()
    initial_infos = {
        "Posição inicial": list(ambiente.position),
        "Estado inicial do grid": list(ambiente.grid),
        "Pontuação inicial": ambiente.score
    }
    infos = []


    for passo in range(10):
        percepcao = ambiente.percept()
        acao, direcao = agente.action(percepcao)
        ambiente.action_in_env(acao, direcao)
        infos.append({
            "Passo": passo + 1,
            "Percepção": percepcao,
            "Ação": acao,
            "Direção": direcao,
            "Posição": list(ambiente.position),
            "Pontuação": ambiente.score,
            "Estado do grid": list(ambiente.grid) 
        })
        
    

    format_simulation_results(initial_infos, infos)


if __name__ == "__main__":
    simular()