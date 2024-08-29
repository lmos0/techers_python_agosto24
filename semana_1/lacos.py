#controle = int(input('Digite quantos carneirinhos você deseja contar: '))

# while controle > 0:
#     print('🐏')
#     controle = controle + 1

#print('Essa linha não faz parte do loop')
#O bloco while irá testar uma condição. Caso a condição seja VERDADEIRA, o bloco de código (identado) será executado. Senão, o bloco de código será ignorado

controle = int(input('Digite um número para iniciar a contagem regressiva'))

while controle >= 0:
    print(controle)
    controle = controle - 1

#Cada ciclo de execução de um laço, ou de um bloco de loop, é chamado de Iteração ou Iteration 