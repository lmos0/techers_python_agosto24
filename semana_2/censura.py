palavra_censurada = input('Digite a palavra a ser censurada: ')

caracter_de_censura = '*******'

texto = input('Digite uma frase: ')

texto_censurado = texto.replace(texto, caracter_de_censura)

print(texto_censurado)