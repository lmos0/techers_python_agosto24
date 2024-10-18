"""

ValueError 

Coloca um argumento com o tipo de dado incorreto dentro de uma função

"""

# while True:

#     try:
#         numero = int(input('Digite um número: '))
#         print(numero)
#     except ValueError:
#         print('Por favor, digite apenas numerais')

"""
TypeError

Quando se tenta executar uma operação com tipos de dados incompetíveis

"""

# try:
#     resultado = 5 + "pato"

# except TypeError:
#     print('Erro: Não é possível somar uma string com um numeral')

"""
IndexError
- Ocorre quando você tenta acessar um índice que não existe em uma lista 


"""
# try:
#     lista = [1,2,3,4,5]
#     print(lista[12])
# except IndexError:
#     tamanho_lista = len(lista)
#     print(f'Não há esse elemento na lista. A lista tem apenas {tamanho_lista} elementos ')

"""
KeyError

Quando se tenta acessar uma chave que não existe em um dicionário

"""

# try:
#     dicionario = {'nome': 'João',
#                 'idade': 46}
#     print(dicionario['email'])
# except KeyError:
#     print('Erro: a chave buscada não existe no dicionário')

"""
FileNotFoundError

Ocorre quando você tenta manipular um arquivo que não existe

"""

try:
    arquivo = open('arquivo_que_na_existe.txt', 'r')
except FileNotFoundError:
    print('Erro: arquivo não encontrado')
