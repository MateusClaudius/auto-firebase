import csv

path_lista = [
    ['entrada', 'saida'],
    ['c:\\Users\\mateus.santos_acesso\\Downloads', 'c:\\Users\\mateus.santos_acesso\\Documents\\firebase'],
    ['c:\\Users\\mateus.santos_acesso\\Downloads', 'c:\\Users\\mateus.santos_acesso\\Documents\\firebase']
]

'''with open('teste.csv', 'w', newline='', encoding='utf-8') as aquivo:
    for linha in path_lista:
        aquivo.write(str(linha) + '\n')'''

with open('teste2.csv', 'w', newline='', encoding='utf-8') as arquivo:

    escritor = csv.writer(arquivo, delimiter=';')

    for linha in path_lista:
        escritor.writerow(linha)
