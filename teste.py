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
