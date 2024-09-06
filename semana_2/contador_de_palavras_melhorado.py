trecho = input('Digite um texto: ')

lista_de_palavra = trecho.split()

contagem_de_palavras = {}

for palavra in lista_de_palavra:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)

