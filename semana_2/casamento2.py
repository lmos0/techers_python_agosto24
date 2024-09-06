lista_de_casamento = []

while True:
    convidado = input('Adicione um convidado. Ou Pressione "0" para SAIR    ').title().strip()
    if convidado == '0':
        break
    else:
        lista_de_casamento.append(convidado)

print(f'Lista Concluída. Os convidados são {lista_de_casamento} ')

nome_a_ser_buscado = input('Digite o nome do convidado: ').title().strip()

for nome in lista_de_casamento:
    if nome_a_ser_buscado in lista_de_casamento:
        print(f'{nome_a_ser_buscado} está na lista de convidados')
        break

    else:
        print(f'{nome_a_ser_buscado} não está na lista de convidados')
        break
