"""
Crie um programa que receba a idade de uma pessoa e a classifique em uma
das seguintes categorias:

Criança: até 12 anos

Adolescente: de 13 a 18 anos

Adulto: de 19 a 64 anos

Idoso: acima de 65 anos

Exiba a categoria de classificação da pessoa.

"""

idade = int(input('Digite a idade do usuário: '))
categoria = None #Reservando um espaço na memória para a variável e inicializando ela como vazia.

if idade <= 12: #Criança: até 12 anos
    categoria = 'Criança'

elif idade <= 18: # Adolescente: de 13 a 18 anos
    categoria = 'Adolescente'

elif idade <= 64: #Adulto: de 19 a 64 anos
    categoria = 'Adulto'

else: #Idoso: acima de 65 anos
    categoria = 'Idoso'

print(f'O usuário tem {idade} anos e é considerado {categoria} ')