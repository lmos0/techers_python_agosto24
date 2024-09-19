import os

nome = input('Qual seu nome: ')

file = open('nomes.txt', 'a')

#primeiro parâmetro = nome do arquivo que será no manipulado e na variável 'file'
#segundo parâmetro = modo de manipulação do arquivo. w = (write) Escrever um novo arquivo a (append) = adicionar informação arquivo

file.write(f"{nome}\n")

file.close()
