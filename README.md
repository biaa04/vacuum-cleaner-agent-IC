# Agente Aspirador Inteligente

Este projeto implementa uma simulação de agentes aspiradores em um ambiente bidimensional, comparando dois tipos de agentes:

- Agente Simples (Reativo)
- Agente com Modelo (Baseado em Memória)

O objetivo é analisar o comportamento, eficiência e tomada de decisão de cada agente ao limpar um ambiente com sujeira e obstáculos.

## Como Funciona

O ambiente é representado por uma matriz (grid), onde cada célula pode ser:

- "sujo" → precisa ser limpo
- "limpo" → já está limpo
- "obst" → obstáculo

O agente começa na posição (0, 0) e executa ações com base na percepção do ambiente.

## Tipos de Agentes

### Agente Simples

- Não possui memória
- Age apenas com base na percepção atual
- Pode repetir movimentos desnecessários
- Não evita obstáculos de forma inteligente

Comportamento:

- Se estiver em "sujo" → limpa
- Se estiver em "limpo" → move aleatoriamente
- Se encontrar "obst" → sofre dano

### Agente com Modelo

- Possui memória da última direção
- Evita voltar imediatamente para a posição anterior
- Mais eficiente na exploração do ambiente

Diferencial:

- Reduz movimentos redundantes
- Toma decisões um pouco mais inteligentes

## Execução

Para rodar o programa:

python main.py

Você verá um menu:

Agente Aspirador
1. Agente Simples
2. Agente Modelo
3. Sair

Escolha o tipo de agente para iniciar a simulação.

## Regras da Simulação

- Limpar sujeira → +1 ponto
- Limpar célula limpa → -1 ponto
- Colidir com obstáculo → +1 dano
- Tentar sair do grid → +1 dano
- Máximo de 200 passos ou até limpar tudo
