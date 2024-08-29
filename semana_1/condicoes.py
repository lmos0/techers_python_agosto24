x = int(input('Qual valor de X: '))
y = int(input('Qual valor de Y: '))

if x < y:
    print('X é menor do que Y')

elif x > y:
    print('X é maior do que Y')
    #Junção das palavra 'if' e 'else'. Elif busca a primeira condição verdadeira e interrompe os teste, assim que ela é encontrada.

elif x == y:
    print('X é igual a Y')