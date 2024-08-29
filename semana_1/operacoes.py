texto = "esse é texto que eu quero que apareça no meu programa" 
#Quando utilizamos "" '' estamos trabalhando com tipo de dado chamado STR (ou String) => Sequência de caracteres

x = int(input('Digite o valor de X: '))
# é um tipo dado chamado INT (inteiro)

y = int(input('Digite o valor de Y: '))
# Esse tipo de dado é chamado de FLOAT (número com casas decimais)

int() #Conversores de tipo => Transforma dado guardado na variável em um INT
str() #Conversores de tipo => Transforma dado guardado na variável em um STR
float() #Conversores de tipo => Transforma dado guardado na variável em um FLOAT

adicao = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y 
modulo = x // y #Descobrir qual é resultado da divisão, ignorando o resto
exponenciacao = x ** y
resto = x % y #% não quer dizer porcentagem. Essa operação retorna o resto de uma divisão

print(adicao)
print(subtracao)
print(multiplicacao)
print(divisao) #Quando trabalhamos com operação divisão, o Python converte a variável automaticamente para float
print(exponenciacao)
print(modulo)
print(resto)