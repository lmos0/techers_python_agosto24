preco_lojas = {
    'camiseta':50,
    'calça':100,
    'sapato':60
}


for item in preco_lojas: #Imprimir as chaves durante um loop
    print(item)


for item in preco_lojas: #Imprimir os valores durante um loop. nome_do_dicionario[nome_da_chave]
    print(preco_lojas[item])

for item in preco_lojas: #Combinação dos dois, separados por vírgula
    print(f' O item {item} custa {preco_lojas[item]}')