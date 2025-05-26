import os
for arquivo in os.listdir(f'c:\\Users\\mateus.santos_acesso\\Downloads'):
    if 'json' in arquivo:
        print(arquivo)
        os.rename(f'c:\\Users\\mateus.santos_acesso\\Downloads\\{arquivo}', f'C:\\Users\\mateus.santos_acesso\\Documents\\repositorios\\auto-firebase\\firebase\\{arquivo[:13].title() + '.json'}')

