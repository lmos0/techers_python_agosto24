import csv 

prova_1 = []
prova_2 = []
prova_3 = []
nomes = []
medias = []


#notas de cada prova
with open('notas.csv', mode='r') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv) #Pular linha antes de iniciar leitura do arquivo
    for linha in leitor_csv:
        nomes.append(linha[0])
        prova_1.append(float(linha[1]))
        prova_2.append(float(linha[2]))
        prova_3.append(float(linha[3]))

for nota in range(len(nomes)):
    media_aluno = (prova_1[nota] + prova_2[nota] + prova_3[nota]) / 3
    medias.append(media_aluno)
    print(f'{nomes[nota]}: {media_aluno}')

aluno = input('Digite o nome do aluno: ')


if aluno in nomes:
    indice = nomes.index(aluno) #Método Index retorna a posição do elemento pedido ex[0] 
    print(f'A média do {aluno} foi {medias[indice]}') #Os índices das notas, prova1,prova2, média são exatamentes os mesmos

else:
    print('Aluno não encontrado')

