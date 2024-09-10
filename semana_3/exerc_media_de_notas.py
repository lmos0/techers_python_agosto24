"""
Crie um programa que solicita ao usuário que insira várias notas (valores entre 0 e 10). O programa deve continuar pedindo notas até que o usuário insira um valor negativo. Em seguida, exiba a média das notas válidas inseridas.

"""

#solicita usuario = input() fazer conversão para float()

#criar loop até que usuário insira um valor negativo

#inserir média: print()

lista_de_notas = []

while True:
    nota = float(input('Digite a nota a ser insirida no sistema. Caso deseja encerrar o programa, digite um número negativo: '))
    if nota < 0:
        break 
    if nota >=0 and nota <= 10: #Se nota menor que 10 e maior que 0, quer dizer que é uma nota válida
        lista_de_notas.append(nota)
        print(lista_de_notas)
    else:
        print('Por favor, insira uma nota entre 0 e 10')
    
    

# total = 0

# for n in lista_de_notas:
#     total = total + n # media += n

# media = total / len(lista_de_notas)

media =  sum(lista_de_notas)/len(lista_de_notas)

print(f'A média da turma foi {media}')


