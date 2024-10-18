while True:
    try:
        x = int(input('Digite um número: '))

        y = int(input('Digite outro número: '))

        resultado = x/y

        print(resultado)

        if x < 0 or y < 0:
            break
    except ZeroDivisionError:
        pass