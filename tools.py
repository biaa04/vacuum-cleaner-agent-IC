import json

def create_json_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def format_simulation_results(initial_infos, infos):

    data = {
        "Informações Iniciais": initial_infos,
        "Passos": infos
    }

    create_json_file(data, "simulation_results.json")