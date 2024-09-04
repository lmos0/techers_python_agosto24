"""
Crie um programa que receba três números inteiros do usuário e determine
qual é o maior entre eles.
Exiba o maior número encontrado

"""

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
num3 = int(input('Digite o terceiro número inteiro: '))

maior_numero = num1

if num2 > maior_numero:
    maior_numero = num2

if num3 > maior_numero:
    maior_numero = num3

#Interpolação de Strings => Colocar variáveis dentro de uma string (sequência de texto)
# {} chaves com placeholders 
print(f"O maior número entre {num1},{num2} e {num3} é: {maior_numero} ")

