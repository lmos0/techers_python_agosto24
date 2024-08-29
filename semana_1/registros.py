nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: ')) # int() Certificar que o Python irá entender o valor digitado como um número inteiro 
profissao = input('Digite sua profissão: ')

#Quando se usa o método input() (palavra chave que executa uma ação específica no código), o Python irá entender o valor recebido como TEXTO

if idade < 18:
    print('Menor de idade. Você não pode entrar!') #Essa linha só será executada caso a condição da linha 7 seja verdadeira
else:
    print('Usuário maior de idade. Você pode entrar no estabelecimento')
