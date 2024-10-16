#eval()
# Lê uma string e retorna/executa o código em python representado na string


#funções lambdas => funções anonimas 

def adicao(x,y):
    resultado = x+y
    return resultado


adicao(3,5)

add = lambda x,y: x+y

print(add(2,3))