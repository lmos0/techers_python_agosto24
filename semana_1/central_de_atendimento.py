#Central Atendimente onde o usuário vai digitar 1, 2 ou 3 para falar com departamentos diferentes
#O programa precisa receber um input do usuário e direcioná-lo para o setor correto
# Uma vez escolhido o setor financeiro, eu quero ter a opção de acessar alguns serviços
 # Baixar Boleto
 #Confirmar  Cadastro
 #Falar com atendente

print('Bem-vindo ao atendimento automatizado da Techers')

print('Digite 1 para falar com setor de vendas') #Quando usamos o método print(), /n é colocado automaticamente pelo Python
print('Digite 2 para falar com o setor pedagógico')
print('Digite 3 para falar com o setor financeiro')

escolha_do_usuario = input('Escolha a opção desejada! \n') # \n informa quebra-linha dentro da string

if escolha_do_usuario == '1':  # 1 é diferente (!=) de "1"
    print('Você está falando com o setor de vendas! Como posso ajudá-lo? ')

elif escolha_do_usuario == '2':
    print('Você está falando com o setor Pedagógico. Por favor, aguarde nosso atendente ')

elif escolha_do_usuario == '3':
    print('Você está falando com setor financeiro. Por favor selecione uma das seguintes opções: ')
    print('1 - Baixar Boletos')
    print('2 - Atualizar cadastro de e-mail')
    print('3 - Falar com um dos nossos atendentes ')

    escolha_do_usuario_2 = input('Escolha a opção desejada! \n')

    if escolha_do_usuario_2 == '1':
        print('Boleto baixado com sucesso!')
    elif escolha_do_usuario_2 == '2':
        print('Endereço de e-mail atualizado com sucesso')
    elif escolha_do_usuario_2 == '3':
        print('O atendente vai entrar em contato em breve')
    else:
        print('Opção inválida. Digite 1, 2 ou 3')

else:
    print('Opção inválida. Digite 1, 2 ou 3')


