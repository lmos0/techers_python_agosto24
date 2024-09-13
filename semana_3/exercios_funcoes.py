"""
Contador de vogais:

Usa uma compreensão de lista com a função sum() para contar as vogais.
Converte o texto para minúsculas para simplificar a verificação.

"""

def contar_vogais(texto):

    quantidade_de_vogais = 0

    vogais = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    for letra in texto:
        if letra in vogais:
            quantidade_de_vogais += 1
    
    return quantidade_de_vogais

"""
Verificador de palíndromo:

Remove espaços e converte para minúsculas para uma comparação mais precisa.

"""

def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "") #Certificar que os espaços não irão atrapalhar a checagem do palíndromo
    return texto == texto[::-1] # Comparação que irá retornar True ou False, se o texto invertido for igual ao texto original é porque é um palíndromo 

#print(eh_palindromo('radar'))


"""
Conversor de temperatura:

Implementa a fórmula de conversão de Celsius para Fahrenheit.

"""

def conversor_de_temperatura(celsius):
    return (celsius * 9/5) + 32

# print(conversor_de_temperatura(23))

# print(conversor_de_temperatura(95))

"""
Gerador de tabuada:

Usa um loop for para gerar a tabuada de 1 a 10.
Utiliza f-string para formatar a saída.

"""

def tabuada(numero):
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')

tabuada(5)
tabuada(65)