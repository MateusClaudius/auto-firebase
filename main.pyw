import os
import json
from tkinter import *
from tkinter import filedialog

window = Tk()
entrada = saida = ''
txt_entrada = StringVar()
txt_saida = StringVar()
msg_terminal = StringVar()
config_path = 'config.json'

cores = {
    'cinza': '#1e1e1e',
    'laranja': '#ffa000',
    'branco': "#c0c0c0"
    }

def carregar_path():
        global entrada, saida

        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                entrada = dados['entrada']
                saida = dados['saida']

def salvar():
    global entrada, saida

    if entrada != "" and saida != "":
        with open(config_path, 'w', encoding='utf-8') as arquivo:
            json.dump({'entrada': entrada, 'saida': saida}, arquivo, ensure_ascii=False, indent=4)

def carregar_labels():
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                txt_entrada.set(dados['entrada'])
                txt_saida.set(dados['saida'])

class Funcoes:

    def finalizar():
        exit()
    
    def caminho(file):
        msg_terminal.set('')
        global entrada, saida

        if file == 'E':
            entrada = filedialog.askdirectory()
            print(entrada)
        elif file == 'S':
            saida = filedialog.askdirectory()
            print(saida)
        
        salvar()
        carregar_labels()
        #carregar_path()
    
    def apagar():
        global saida

        os.startfile(saida)
        #window.destroy()
        msg_terminal.set('Arquivos deletados com sucesso!')

        print(saida)
        for arquivo in os.listdir(saida):
            if 'json' in arquivo:
                caminho_completo = os.path.join(saida, arquivo)
                os.remove(caminho_completo)
    
    def converter():
       global entrada, saida

       os.startfile(saida)
       #window.destroy()
       msg_terminal.set('Conversão realizada com sucesso!')

       print(entrada, saida)
       for arquivo in os.listdir(entrada):
            if 'json' in arquivo:
                os.rename(f'{entrada}\\{arquivo}', f'{saida}\\{arquivo[:13].title() + '.json'}')

class Janela(Funcoes):
    def __init__(self):
        carregar_path()
        carregar_labels()
        self.tela()
        self.botoes()
        window.mainloop()
    
    def tela(self):
        window.title('Automação FireBase')
        window.configure(background=cores['cinza'])
        window.geometry('720x252')
        window.resizable(False, False)
    
    def botoes(self):
        self.label = Label(window, text='Selecione a pasta onde os arquivos .json estão:', bg=cores['cinza'], fg='white', font=('Arial', 11, 'bold'))#Label de seleção da pasta de entrada
        self.label.place(relx=0.05, rely=0.20)

        self.label = Label(window, textvariable=txt_entrada, bg=cores['cinza'], fg=cores['branco'], font=('Arial', 9))#Label que irá mostrar o caminho da pasta de entrada
        self.label.place(relx=0.05, rely=0.28)

        self.selecionar_1 = Button(window, text='Selecionar Pasta', command=lambda: Funcoes.caminho(file='E'), bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))#Botão para delecionar pasta de entrada
        self.selecionar_1.place(relx=0.75, rely=0.18)

        self.label = Label(window, text='Selecione a pasta onde os arquivos .json estarão após a conversão:', bg=cores['cinza'], fg='white', font=('Arial', 11, 'bold'))#Label de seleção da pasta de saída
        self.label.place(relx=0.05, rely=0.42)

        self.label = Label(window, textvariable=txt_saida, bg=cores['cinza'], fg=cores['branco'], font=('Arial', 9))#Label que irá mostrar o caminho da pasta de saída
        self.label.place(relx=0.05, rely=0.50)

        self.selecionar_2 = Button(window, text='Selecionar Pasta', command=lambda: Funcoes.caminho(file='S'), bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))#Botão para delecionar pasta de saída
        self.selecionar_2.place(relx=0.75, rely=0.4)

        self.iniciar = Button(window, text='Iniciar conversão', command=Funcoes.converter, bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))#Botão de iniciar conversão
        self.iniciar.place(relx=0.05, rely=0.7)

        self.deletar = Button(window, text='Deletar arquivos', command=Funcoes.apagar, bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))#Botão que apaga todos os arquivos .json da pasta saída
        self.deletar.place(relx=0.24, rely=0.7)

        self.fechar = Button(window, text='Fechar programa', command=Funcoes.finalizar, bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))#Botão que fecha a automação
        self.fechar.place(relx=0.423, rely=0.7)

        self.label = Label(window, textvariable=msg_terminal, bg=cores['cinza'], fg='green', font=('Arial', 11, 'bold'))#Label que exibe o resultado da operação
        self.label.place(relx=0.626, rely=0.72)

Janela()
