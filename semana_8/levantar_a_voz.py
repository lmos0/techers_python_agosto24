while True:
    try:
        x = int(input('Digite um número: (JAMAIS DIGITE 4) '))

        y = int(input('Digite outro número: (JAMAIS DIGITE 4) '))

        if x == 4 or y == 4:
            raise ValueError('Eu não quero que você digite 4 no meu programa')

        resultado = x/y

        print(resultado)

    except ZeroDivisionError:
        print('Erro: Não é possível dividir por zero')
    