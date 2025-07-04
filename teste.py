import json

jogadores = {
    "jogadores": [
        {
            "nome": "Stephen Curry",
            "time": "Golden State Warriors"
        },
        {
            "nome": "Lebron James",
            "time": "Los Angeles Lakers"
        }
    ]
}

with open('path.json', 'w', encoding='utf-8') as arquivo:
    json.dump(jogadores, arquivo, ensure_ascii=False, indent=4)

with open('path.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    print(dados['jogadores'][0]['nome'], dados['jogadores'][1]['nome'])
