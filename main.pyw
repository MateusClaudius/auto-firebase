import os
from tkinter import *
from tkinter import filedialog

window = Tk()
entrada = saida = ''

cores = {
    'cinza': '#1e1e1e',
    'laranja': '#ffa000'
    }

class Funcoes:

    def finalizar():
        exit()
    
    def caminho(file):
        global entrada
        global saida

        if file == 'E':
            entrada = filedialog.askdirectory()
            print(entrada)
        elif file == 'S':
            saida = filedialog.askdirectory()
            print(saida)
    
    def converter():
       global entrada
       global saida

       os.startfile(saida)
       window.destroy()

       print(entrada, saida)
       for arquivo in os.listdir(entrada):
            if 'json' in arquivo:
                os.rename(f'{entrada}\\{arquivo}', f'{saida}\\{arquivo[:13].title() + '.json'}')

class Janela(Funcoes):
    def __init__(self):
        self.tela()
        self.botoes()
        window.mainloop()
    
    def tela(self):
        self.tela = window
        window.title('Automação Firebase')
        window.configure(background=cores['cinza'])
        window.geometry('720x252')
        window.resizable(False, False)
    
    def botoes(self):
        self.label = Label(window, text='Selecione a pasta onde os arquivos .json estão:', bg=cores['cinza'], fg='white', font=('Arial', 11, 'bold'))
        self.label.place(relx=0.05, rely=0.19)

        self.selecionar_1 = Button(window, text='Selecionar Pasta', command=lambda: Funcoes.caminho(file='E'), bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))
        self.selecionar_1.place(relx=0.75, rely=0.18)

        self.label = Label(window, text='Selecione a pasta onde os arquivos .json estarão após a conversão:', bg=cores['cinza'], fg='white', font=('Arial', 11, 'bold'))
        self.label.place(relx=0.05, rely=0.41)

        self.selecionar_2 = Button(window, text='Selecionar Pasta', command=lambda: Funcoes.caminho(file='S'), bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))
        self.selecionar_2.place(relx=0.75, rely=0.4)

        self.iniciar = Button(window, text='Iniciar conversão', command=Funcoes.converter, bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))
        self.iniciar.place(relx=0.05, rely=0.6)

        self.fechar = Button(window, text='Fechar programa', command=Funcoes.finalizar, bd=4, bg=cores['laranja'], font=('Arial', 10, 'bold'))
        self.fechar.place(relx=0.24, rely=0.6)

Janela()
