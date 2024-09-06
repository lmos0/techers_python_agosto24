vogais = ['a','e','i','o','u']

palavra = input('Digite a palavra: ')

#string/palavra é uma lista de caracteres. Portanto, ela é iteravel, ou seja, pode ser percorrida por um loop for

quantidade_de_vogais = 0

for letra in palavra:
    if letra in vogais:
       quantidade_de_vogais +=1
       #é exatamente a mesma coisa que quantidade_de_vogais = quantidade_de_vogais + 1

print(quantidade_de_vogais)