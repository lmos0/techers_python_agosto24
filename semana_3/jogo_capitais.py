import random

#jamais nomei seu arquivo .py com o nome de um módulo ou bibliotca o qual você vai importar

dicionario_capitais_paises = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "Canadá": "Ottawa",
    "Espanha": "Madrid",
    "Irlanda": "Dublin",
    "França": "Paris"

}

tentativas = 3
pontos = 0

#chaves são os nomes dos países e os valores são os nomes das capitais

lista_de_capitais = list(dicionario_capitais_paises.keys())


#random.choice é um método feito exclusivamente para listas. 
#Existe o método .keys(), que é um método relacionado a dicionários => Ele pega todas as CHAVES dentro de um dicionário e devolve um objeto >SEMELHANTE< a uma lista 

#Qual problema?
#Não é possível usar métodos relacionados às listas (nome_da_lista.) com esse objeto SEMELHANTE a uma lista, retornado pelo .keys()

#Por essa razão, é necessário converter o objeto a uma lista de fato. Usando o método list(objeto_semelhante_a_lista)

#Feita a conversão, eu consigo utilizar métodos relacionados a listas. INCLUSIVE o random.choice

print('Caso deseje encerrar o jogo, digite a palavra "sair" ')

while tentativas > 0 and len(lista_de_capitais) > 0:
    
    capital_da_rodada = random.choice(lista_de_capitais)

    resposta_do_usuario = input(f'Qual é a capital de {capital_da_rodada}? ').title().strip()
    

    if resposta_do_usuario == dicionario_capitais_paises[capital_da_rodada]:
        pontos += 1
        print('Parabéns, você acertou!')
        print(f'Você tem atualmente {pontos} pontos')
        print(f'Você ainda tem {tentativas} chances')
        lista_de_capitais.remove(capital_da_rodada)
    
    elif resposta_do_usuario == 'Sair':
        break

    else:
        print('Você errou!')
        tentativas -= 1
        print(f'Você ainda tem {tentativas} chances')
       

print('Jogo Encerrado!')
print(f'A resposta correta era {dicionario_capitais_paises[capital_da_rodada]}')
print(f'Você fez {pontos} pontos')