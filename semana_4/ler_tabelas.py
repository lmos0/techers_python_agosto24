import os, csv

with open('notas.csv', mode='r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    cabecalho = next(leitor_csv) #Pular uma linha. 
    for linha in leitor_csv:
        print(linha)