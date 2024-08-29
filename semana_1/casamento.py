lista_de_casamento = []

print('Caso deseje inserir um novo convidado digite: 1 \n' )

print('Caso deseje remover um convidado digite: 2 \n')

print('Caso deseje visualizar a lista atual de convidados digite: 3 \n')

print('Caso deseje visualizar a quantidade de convidados, digite: 4 \n')

print('Para encerrar o programa digite: 0 \n')

while True:

    input_usuario = input('Digite a opção desejada: ')

    if input_usuario == '1':
        nome_convidado = input('Digite o nome do convidado: ')
        lista_de_casamento.append(nome_convidado)
    
    if input_usuario == '2':
        convidado_removido = input('Digite o nome do convidado a ser removido da lista: ')
        lista_de_casamento.remove(convidado_removido)
    
    if input_usuario == '3':
        print('##############################')
        print(lista_de_casamento)
        print('##############################')

    if input_usuario == '0':
        break

print('Lista de Casamento finalizada')
print('Os convidados são:', lista_de_casamento)
