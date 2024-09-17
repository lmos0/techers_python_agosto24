def calculadora(num1:int, num2:int, operacao:str):
   
    """

    O primeiro argumento deve ser um numeral, bem como o segundo elemento. O terceiro elemento deve ser um sinal de operação matemática
    adição +
    subrtração -
    multiplicação x
    divisão /
    """
    # Docstring utilizando """ """ é a forma de usar strings para criar documentação de funções
    
    if operacao == "+":
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == 'x':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    
    else:
        return 'Operação Inválida. Escolha entre +, -, x, /'
    

resultado = calculadora('+', 12, 19)
#Qundo for chamar a função a ordem dos elementos importa

print(resultado)

calculadora()