import os

with open('nomes.txt', 'r') as file:
    #file.write(f"{nome}\n")
    linhas = file.readlines()
    
    for linha in linhas:
        print('Bom dia', linha.rstrip())

#primeiro parâmetro = nome do arquivo que será no manipulado e na variável 'file'
#segundo parâmetro = modo de manipulação do arquivo. 
# w = (write) Escrever um novo arquivo a (append) = adicionar informação arquivo

# r = (read). Abrir em modo de leitura 
