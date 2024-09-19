import os 

lista_de_convidados = []

with open('lista_de_convidados.txt') as file:  #as file é a mesma coisa file = 
    for linha in file:
        lista_de_convidados.append(linha.rstrip())


lista_de_convidados.sort() #Coloca em ordem alfabetica

for nome in sorted(lista_de_convidados):
    with open('lista_de_convidados_em_ordem_alfabetica.txt', 'w') as new_file:
        for linha in lista_de_convidados:
            new_file.write(f'{linha}\n')
