import csv

with open('path.csv', 'r', newline='', encoding='utf-8') as arquivo:

    leitor = csv.reader(arquivo, delimiter=';')

    for indice, linha in enumerate(leitor):
        print(indice + 1, linha)
