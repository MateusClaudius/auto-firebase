import csv

with open('path.csv', 'r', newline='', encoding='utf-8') as arquivo:
    
    leitor = csv.reader(arquivo)

    print(list(leitor)[0])

    for linha in leitor:
        print(linha)
