x = int(input('Qual valor de X: '))
y = int(input('Qual valor de Y: '))

if x < y:
    print('X é menor do que Y') #identação é o espaço que indica que a linha está atrelada a condição verdadeira da linha anterior

elif x > y:
    print('X é maior do que Y')
    #Junção das palavra 'if' e 'else'. Elif busca a primeira condição verdadeira e interrompe os teste, assim que ela é encontrada.

elif x == y: #Quando se deseja fazer uma comparação, usa-se o sinal duplo de igual '==' 
    print('X é igual a Y')