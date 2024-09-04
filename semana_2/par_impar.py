"""
- Crie um programa que receba um número inteiro do usuário e verifique se ele é par ou ímpar. input()
- Exiba uma mensagem informando se o número é par ou ímpar. print()
"""

numero_escolhido_pelo_usuario = int(input('Digite um número: '))

if numero_escolhido_pelo_usuario % 2 == 0:
    print('O número é par')

else:
    print('O número é impar')
