"""

Crie um programa para armazenar contatos (nomes) e números de telefone em um dicionário.

Permitir adicionar, consultar, modificar e remover contatos.

Utilize um dicionário onde as chaves são os nomes dos contatos e os valores são os números de telefone.

"""

agenda = {}

while True:
    
    print('#######################################################################################')
    print('\nAgenda Telefônica')
    print('\n1 - Adicionar contato') #\n informa para str que é necessário dar um enter
    print('2 - Consultar contato')
    print('3 - Atualizar contato')
    print('4 - Remover contato')
    print('5 - Sair\n')
    print('#######################################################################################')

    opcao = input('Escolha uma opção: \n')

    if opcao == '1':
        nome_do_contato = input('Digite o nome do contato: ')
        telefone_do_contato = input('Digite o telefone: ')
        agenda[nome_do_contato] =  telefone_do_contato # dicionario[chave] = atribuindo o valor ex {'luis': 3212:2211}
        print('Contato adicionado com sucesso')
    elif opcao == '2':
        nome_a_ser_consultado = input('Digite o nome do contato: ')
        if nome_a_ser_consultado in agenda:
            print(f'{nome_a_ser_consultado} : {agenda[nome_do_contato]}')
        else:
            print('Contato não encontrado.')
    
    elif opcao == '3':
        nome_a_ser_alterado = input('Digite o nome do contato: ')
        if nome_a_ser_alterado in agenda:
            novo_telefone = input('Digite o novo número: ')
            agenda[nome_do_contato] = novo_telefone
            print('Contato Atualizado!')
        else:
            print('Contato não encontrado')

    elif opcao == '4':
        nome_a_ser_excluido = input('Digite o nome do contato: ')
        if nome_a_ser_excluido in agenda:
            del agenda[nome_do_contato]
            print('Contato removido!')
        
        else:
            print('Contato não encontrado!')
    
    elif opcao == '5':
        print('Agenda encerrada...')
        break 

    else:
        print('Opção inválida')
