paises_america_do_sul = []

paises_america_do_sul = ['Brasil', 'Argentina', 'Venezuela', 'Peru']

paises_america_do_sul.append('Uruguai')
print(paises_america_do_sul)
paises_america_do_sul.insert(0, 'Paraguai')
print(paises_america_do_sul)

metade_america_do_sul = paises_america_do_sul[0:3] # Slicing é uma forma de criar uma nova lista a partir de uma lista já existente. 
#Usamos o colchete, colocamos  o primeiro index do elemento que desejamos : até o primeiro elemento que >não< desajamos inserir
print('Essa é lista dividida ', metade_america_do_sul)

print(paises_america_do_sul)
paises_america_do_sul.sort(reverse=True) #Coloquei a lista em ordem alfabética crescente
print(paises_america_do_sul)

