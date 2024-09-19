import os, csv

with open('cadastro.csv', mode='w', newline='', encoding='utf8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerow(['Nome', 'Idade', 'Cidade']) #Escrevi minha primeira linha. Usando uma lista pra posicionar os elementos
    escritor_csv.writerows([['João', '25', 'São Paulo'], ['Mariana', '38', 'Brasília'], ['Arthur', '20', 'Uberlândia']])



# listas = [[1,2,3], ['abelha', 'mel', 'outro'], [True, False, 3.0]]