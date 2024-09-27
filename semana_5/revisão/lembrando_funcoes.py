def maior_menor_igual(x:int,y:int):

    """
    Função que verifica se um numero é maior, menor ou igual a outro número.

    """

    if x > y:
        return f'{x} é maior que {y}'
    
    elif x < y:
        return f'{x} é menor que {y}'
    
    else:
        return f'{x} é igual a {y}'
    


resultado = maior_menor_igual('789','980') #chamei a função e guardei o RETORNO em uma variável
print(resultado) #imprimindo o conteúdo da varíavel, que é o retorno da função