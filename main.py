from environment import Environment as En
from vaccum_agent_simple import VaccumAgentSimple 

def simular():
    ambiente = En(3, 3)
    agente = VaccumAgentSimple()
    print(ambiente.grid)


    for passo in range(10):
        percepcao = ambiente.percept()
        acao, direcao = agente.action(percepcao)
        ambiente.action_in_env(acao, direcao)
        print(f"Passo {passo + 1}: Percepção: {percepcao}, Ação: {acao}, Direção: {direcao}, Posição: {ambiente.position}, Pontuação: {ambiente.score}")
        print(ambiente.grid)

    print("Pontuação final:", ambiente.score)


if __name__ == "__main__":
    simular()