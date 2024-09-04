palavra_a_ser_contada = input('Digite uma palavra: ')

quantidade_de_letras = 0
for letra in palavra_a_ser_contada:

    print(letra)
    quantidade_de_letras = quantidade_de_letras + 1


print(f'A quantidade de letras da palavra {palavra_a_ser_contada} é {quantidade_de_letras}')