def salvar_simulacao_txt(initial_infos, infos, nome_arquivo="resultado_simulacao.txt"):
    """Salva os resultados da simulação em um arquivo de texto.
    O arquivo conterá as informações iniciais da simulação, como a posição inicial do agente   """
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=== Simulação do Agente de Limpeza ===\n\n")

    
        f.write("Informações Iniciais:\n")
        f.write(f"Posição inicial: {tuple(initial_infos['Posição inicial'])}\n")
        f.write(f"Estado inicial do grid: {initial_infos['Estado inicial do grid']}\n")
        f.write(f"Pontuação inicial: {initial_infos['Pontuação inicial']}\n\n")


        for passo in infos:
            f.write(f"Passo {passo['Passo']}:\n")
            f.write(f"  Percepção: {passo['Percepção']}\n")
            f.write(f"  Ação: {passo['Ação']}\n")
            f.write(f"  Direção: {passo['Direção']}\n")
            f.write(f"  Posição: {tuple(passo['Posição'])}\n")
            f.write(f"  Pontuação: {passo['Pontuação']}\n")
            f.write(f"  Danos: {passo['Danos']}\n")
            f.write(f"  Estado do grid: {passo['Estado do grid']}\n\n")

    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")